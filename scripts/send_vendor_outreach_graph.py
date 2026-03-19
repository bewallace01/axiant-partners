#!/usr/bin/env python3
"""
Send vendor outreach email via Microsoft Graph API (OAuth2, no app password).

Uses client credentials flow: app registration with Mail.Send application permission.
Same behavior as send_vendor_outreach.py (dry-run by default, rate limit, suppression,
body/signature) but sends via Graph instead of SMTP.

Requires: pip install msal
Env: AXIANT_TENANT_ID, AXIANT_CLIENT_ID, AXIANT_CLIENT_SECRET, AXIANT_FROM_EMAIL
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_LOG_DIR = BASE_DIR / "_analysis" / "outreach-email"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
GRAPH_SEND_URL = "https://graph.microsoft.com/v1.0/users/{user_id}/sendMail"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_email(addr: str) -> str:
    return addr.strip().lower()


def load_suppression_list(path: Path | None) -> set[str]:
    if not path:
        return set()
    if not path.exists():
        return set()
    suppressed: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        suppressed.add(normalize_email(line))
    return suppressed


def parse_recipients_from_txt(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    candidates = re.split(r"[\s,;]+", raw)
    out: list[str] = []
    for c in candidates:
        c = c.strip()
        if not c:
            continue
        if EMAIL_RE.match(c):
            out.append(normalize_email(c))
    return out


def parse_recipients_from_csv(path: Path, email_column: str) -> list[str]:
    out: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or email_column not in (reader.fieldnames or []):
            raise SystemExit(
                f"CSV missing column '{email_column}'. Found: {reader.fieldnames}"
            )
        for row in reader:
            addr = (row.get(email_column) or "").strip()
            if addr and EMAIL_RE.match(addr):
                out.append(normalize_email(addr))
    return out


def dedupe_keep_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
    return out


def default_subject() -> str:
    return "Free embed: payment calculator for your site"


def default_body() -> str:
    return (
        "Hi,\n\n"
        "I'm with Axiant Partners — we help equipment and dealer sites offer financing to buyers.\n\n"
        "We have a free embeddable calculator so visitors can estimate monthly payments on your product or listing pages. "
        "Teams use it so buyers self-check budget before sales spends time on unqualified leads.\n\n"
        "Preview and copy the embed code (usually a few minutes to add):\n"
        "https://www.axiantpartners.com/embed-calculator/\n\n"
        "No charge for the embed. If this isn't useful, reply unsubscribe and I won't follow up.\n"
    )


def load_signature(path: Path | None) -> str:
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_log_row(log_path: Path, row: dict) -> None:
    is_new = not log_path.exists()
    ensure_dir(log_path.parent)
    with log_path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["timestamp_utc", "to", "status", "detail"],
        )
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def get_token(tenant_id: str, client_id: str, client_secret: str) -> str:
    try:
        import msal
    except ImportError:
        raise SystemExit(
            "Missing dependency: pip install msal\n"
            "See scripts/vendor_outreach_graph.md for setup."
        )
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    if "access_token" not in result:
        err = result.get("error_description") or result.get("error", "unknown")
        raise SystemExit(f"Graph token failed: {err}")
    return result["access_token"]


def send_one_graph(
    *,
    access_token: str,
    from_email: str,
    to_addr: str,
    subject: str,
    body: str,
    reply_to: str | None,
) -> None:
    """Send a single email via Microsoft Graph sendMail API."""
    url = GRAPH_SEND_URL.format(user_id=urllib.parse.quote(from_email, safe=""))
    message: dict = {
        "message": {
            "subject": subject,
            "body": {"contentType": "Text", "content": body},
            "toRecipients": [
                {"emailAddress": {"address": to_addr}},
            ],
        },
        "saveToSentItems": True,
    }
    if reply_to:
        message["message"]["replyTo"] = [
            {"emailAddress": {"address": reply_to}},
        ]
    body_bytes = json.dumps(message).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body_bytes,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.status not in (200, 202):
            raise RuntimeError(f"Graph returned {resp.status}")


def send_messages_graph(
    *,
    access_token: str,
    from_addr: str,
    reply_to: str | None,
    recipients: list[str],
    subject: str,
    body: str,
    dry_run: bool,
    per_email_delay_s: float,
    max_per_run: int,
    log_path: Path,
) -> tuple[int, list[str]]:
    to_send = recipients[:max_per_run]
    if dry_run:
        for to_addr in to_send:
            write_log_row(
                log_path,
                {
                    "timestamp_utc": utc_now_iso(),
                    "to": to_addr,
                    "status": "DRY_RUN",
                    "detail": "Not sent (dry-run)",
                },
            )
        return (0, [])

    sent = 0
    sent_list: list[str] = []
    for to_addr in to_send:
        try:
            send_one_graph(
                access_token=access_token,
                from_email=from_addr,
                to_addr=to_addr,
                subject=subject,
                body=body,
                reply_to=reply_to,
            )
            sent += 1
            sent_list.append(to_addr)
            write_log_row(
                log_path,
                {
                    "timestamp_utc": utc_now_iso(),
                    "to": to_addr,
                    "status": "SENT",
                    "detail": "",
                },
            )
        except Exception as e:
            write_log_row(
                log_path,
                {
                    "timestamp_utc": utc_now_iso(),
                    "to": to_addr,
                    "status": "ERROR",
                    "detail": str(e)[:500],
                },
            )
        if per_email_delay_s > 0:
            time.sleep(per_email_delay_s)

    return (0 if sent == len(to_send) else 2, sent_list)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Send vendor outreach via Microsoft Graph (OAuth2, no app password)."
    )
    parser.add_argument("--input", required=True, help="Path to recipients list (.txt or .csv).")
    parser.add_argument("--email-column", default="email", help="CSV column for email (default: email).")
    parser.add_argument("--suppression", default="", help="Optional suppression list path (bounces, unsubscribes).")
    parser.add_argument("--sent-file", default="", help="Path to track sent emails. Read as suppression + append new sends. Skips re-emailing.")
    parser.add_argument(
        "--from",
        dest="from_addr",
        default=os.environ.get("AXIANT_FROM_EMAIL", "").strip(),
        help="From email (or set AXIANT_FROM_EMAIL).",
    )
    parser.add_argument(
        "--reply-to",
        default=os.environ.get("AXIANT_REPLY_TO", "").strip(),
        help="Reply-To (or set AXIANT_REPLY_TO).",
    )
    parser.add_argument("--subject", default=default_subject(), help="Subject.")
    parser.add_argument("--body-file", default="", help="Optional body file.")
    parser.add_argument(
        "--signature-file",
        default=os.environ.get("AXIANT_SIGNATURE_FILE", "").strip(),
        help="Optional signature file (or set AXIANT_SIGNATURE_FILE).",
    )
    parser.add_argument("--send", action="store_true", help="Actually send (default: dry-run).")
    parser.add_argument("--delay", type=float, default=6.0, help="Seconds between emails (default: 6).")
    parser.add_argument("--max", dest="max_per_run", type=int, default=80, help="Max per run (default: 80).")
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR), help="Log directory.")
    parser.add_argument(
        "--i-understand",
        action="store_true",
        help="Required with --send (safety check).",
    )
    args = parser.parse_args(argv)

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Input not found: {input_path}", file=sys.stderr)
        return 1

    suppressed = load_suppression_list(
        Path(args.suppression).resolve() if args.suppression else None
    )
    sent_file_path = Path(args.sent_file).resolve() if args.sent_file else None
    if sent_file_path and sent_file_path.exists():
        suppressed = suppressed | load_suppression_list(sent_file_path)
    if input_path.suffix.lower() == ".csv":
        recipients = parse_recipients_from_csv(input_path, args.email_column)
    else:
        recipients = parse_recipients_from_txt(input_path)
    recipients = dedupe_keep_order([r for r in recipients if r not in suppressed])

    if not args.from_addr:
        print("Missing from address. Set AXIANT_FROM_EMAIL or use --from.", file=sys.stderr)
        return 1

    body = default_body()
    if args.body_file:
        body = Path(args.body_file).resolve().read_text(encoding="utf-8")
    sig_path = Path(args.signature_file).resolve() if args.signature_file else None
    if load_signature(sig_path):
        body = body.rstrip() + "\n\n" + load_signature(sig_path)

    dry_run = not args.send
    if not dry_run and not args.i_understand:
        print("Refusing to send without --i-understand.", file=sys.stderr)
        return 1

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_dir = Path(args.log_dir).resolve()
    log_path = log_dir / f"send-log-graph-{ts}.csv"

    print(f"Recipients (after dedupe/suppression): {len(recipients)}")
    if sent_file_path:
        print(f"Sent file (suppress + append): {sent_file_path}")
    print(f"Mode: {'DRY_RUN' if dry_run else 'SEND'} (Graph)")
    print(f"Max this run: {args.max_per_run}")
    print(f"Delay: {args.delay:.1f}s")
    print(f"Log: {log_path}")
    print(f"Subject: {args.subject}")
    print(f"From: {args.from_addr}")
    if args.reply_to:
        print(f"Reply-To: {args.reply_to}")
    print()

    if not recipients:
        print("No recipients to process.")
        return 0

    if dry_run:
        for r in recipients[: min(5, len(recipients))]:
            print(f"  - {r}")
        if len(recipients) > 5:
            print(f"  ... and {len(recipients) - 5} more")
        print()
        print("Body preview (first 25 lines):")
        for i, line in enumerate(body.splitlines()[:25], start=1):
            print(f"{i:02d} {line}")
        print()
        code, _ = send_messages_graph(
            access_token="",
            from_addr=args.from_addr,
            reply_to=args.reply_to or None,
            recipients=recipients,
            subject=args.subject,
            body=body,
            dry_run=True,
            per_email_delay_s=0,
            max_per_run=args.max_per_run,
            log_path=log_path,
        )
        return code

    tenant_id = os.environ.get("AXIANT_TENANT_ID", "").strip()
    client_id = os.environ.get("AXIANT_CLIENT_ID", "").strip()
    client_secret = os.environ.get("AXIANT_CLIENT_SECRET", "").strip()
    missing = [k for k, v in [
        ("AXIANT_TENANT_ID", tenant_id),
        ("AXIANT_CLIENT_ID", client_id),
        ("AXIANT_CLIENT_SECRET", client_secret),
    ] if not v]
    if missing:
        print("Missing env: " + ", ".join(missing), file=sys.stderr)
        print("See scripts/vendor_outreach_graph.md for app registration.", file=sys.stderr)
        return 1

    access_token = get_token(tenant_id, client_id, client_secret)
    code, sent_list = send_messages_graph(
        access_token=access_token,
        from_addr=args.from_addr,
        reply_to=args.reply_to or None,
        recipients=recipients,
        subject=args.subject,
        body=body,
        dry_run=False,
        per_email_delay_s=max(0.0, args.delay),
        max_per_run=max(1, args.max_per_run),
        log_path=log_path,
    )
    if sent_list and sent_file_path:
        ensure_dir(sent_file_path.parent)
        with sent_file_path.open("a", encoding="utf-8") as f:
            for addr in sent_list:
                f.write(addr + "\n")
        print(f"Added {len(sent_list)} to sent list: {sent_file_path}")
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
