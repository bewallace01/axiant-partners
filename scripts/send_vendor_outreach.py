#!/usr/bin/env python3
"""
Send a simple vendor outreach email via SMTP.

Safety defaults:
- Dry-run by default (no email sent unless --send is provided)
- Rate-limited sending
- Dedupes recipients
- Optional suppression list to avoid re-emailing addresses

This script intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import ssl
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from typing import Iterable

import smtplib


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_LOG_DIR = BASE_DIR / "_analysis" / "outreach-email"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True)
class SmtpConfig:
    host: str
    port: int
    username: str
    password: str
    use_starttls: bool = True


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
        if not reader.fieldnames:
            return out
        if email_column not in reader.fieldnames:
            raise SystemExit(
                f"CSV missing column '{email_column}'. Found columns: {reader.fieldnames}"
            )
        for row in reader:
            addr = (row.get(email_column) or "").strip()
            if not addr:
                continue
            if EMAIL_RE.match(addr):
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


def build_message(
    *,
    from_addr: str,
    to_addr: str,
    subject: str,
    body: str,
    reply_to: str | None = None,
) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)
    return msg


def get_smtp_config_from_env() -> SmtpConfig:
    host = os.environ.get("AXIANT_SMTP_HOST", "").strip()
    port = int(os.environ.get("AXIANT_SMTP_PORT", "587").strip() or "587")
    username = os.environ.get("AXIANT_SMTP_USER", "").strip()
    password = os.environ.get("AXIANT_SMTP_PASS", "").strip()
    starttls = os.environ.get("AXIANT_SMTP_STARTTLS", "1").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    )

    missing = [k for k, v in {
        "AXIANT_SMTP_HOST": host,
        "AXIANT_SMTP_USER": username,
        "AXIANT_SMTP_PASS": password,
    }.items() if not v]
    if missing:
        raise SystemExit(
            "Missing SMTP env vars: "
            + ", ".join(missing)
            + "\nSee scripts/vendor_outreach_email.md for setup."
        )
    return SmtpConfig(host=host, port=port, username=username, password=password, use_starttls=starttls)


def default_subject() -> str:
    return "Free embed: payment calculator for your site"


def default_body() -> str:
    return (
        "Hi,\n\n"
        "I’m with Axiant Partners — we help equipment and dealer sites offer financing to buyers.\n\n"
        "We have a free embeddable calculator so visitors can estimate monthly payments on your product or listing pages. "
        "Teams use it so buyers self-check budget before sales spends time on unqualified leads.\n\n"
        "Preview and copy the embed code (usually a few minutes to add):\n"
        "https://www.axiantpartners.com/embed-calculator/\n\n"
        "No charge for the embed. If this isn’t useful, reply unsubscribe and I won’t follow up.\n"
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
            fieldnames=[
                "timestamp_utc",
                "to",
                "status",
                "detail",
            ],
        )
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def send_messages(
    *,
    smtp: SmtpConfig,
    from_addr: str,
    reply_to: str | None,
    recipients: list[str],
    subject: str,
    body: str,
    dry_run: bool,
    per_email_delay_s: float,
    max_per_run: int,
    log_path: Path,
) -> int:
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
        return 0

    context = ssl.create_default_context()
    sent = 0

    with smtplib.SMTP(smtp.host, smtp.port, timeout=30) as server:
        if smtp.use_starttls:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
        server.login(smtp.username, smtp.password)

        for to_addr in to_send:
            try:
                msg = build_message(
                    from_addr=from_addr,
                    to_addr=to_addr,
                    subject=subject,
                    body=body,
                    reply_to=reply_to,
                )
                server.send_message(msg)
                sent += 1
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

    return 0 if sent == len(to_send) else 2


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Send vendor outreach emails via SMTP (dry-run by default)."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to recipients list (.txt or .csv).",
    )
    parser.add_argument(
        "--email-column",
        default="email",
        help="CSV column name containing email addresses (default: email).",
    )
    parser.add_argument(
        "--suppression",
        default="",
        help="Optional path to suppression list (one email per line).",
    )
    parser.add_argument(
        "--from",
        dest="from_addr",
        default=os.environ.get("AXIANT_FROM_EMAIL", "").strip(),
        help="From email address (or set AXIANT_FROM_EMAIL).",
    )
    parser.add_argument(
        "--reply-to",
        default=os.environ.get("AXIANT_REPLY_TO", "").strip(),
        help="Optional Reply-To address (or set AXIANT_REPLY_TO).",
    )
    parser.add_argument(
        "--subject",
        default=default_subject(),
        help="Email subject.",
    )
    parser.add_argument(
        "--body-file",
        default="",
        help="Optional text file containing the email body. If omitted, uses built-in template.",
    )
    parser.add_argument(
        "--signature-file",
        default=os.environ.get("AXIANT_SIGNATURE_FILE", "").strip(),
        help="Optional file containing your email signature (appended to body). Or set AXIANT_SIGNATURE_FILE.",
    )
    parser.add_argument(
        "--send",
        action="store_true",
        help="Actually send emails. If omitted, performs a dry-run.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=6.0,
        help="Seconds to wait between emails (default: 6).",
    )
    parser.add_argument(
        "--max",
        dest="max_per_run",
        type=int,
        default=80,
        help="Max emails to send per run (default: 80).",
    )
    parser.add_argument(
        "--log-dir",
        default=str(DEFAULT_LOG_DIR),
        help=f"Directory for logs (default: {DEFAULT_LOG_DIR}).",
    )
    parser.add_argument(
        "--i-understand",
        action="store_true",
        help="Required when using --send. Confirms you understand deliverability/compliance risks.",
    )
    args = parser.parse_args(argv)

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Input not found: {input_path}", file=sys.stderr)
        return 1

    suppression_path = Path(args.suppression).resolve() if args.suppression else None
    suppressed = load_suppression_list(suppression_path)

    if input_path.suffix.lower() == ".csv":
        recipients = parse_recipients_from_csv(input_path, args.email_column)
    else:
        recipients = parse_recipients_from_txt(input_path)

    recipients = dedupe_keep_order([r for r in recipients if r not in suppressed])

    if not args.from_addr:
        print(
            "Missing from address. Provide --from or set AXIANT_FROM_EMAIL.",
            file=sys.stderr,
        )
        return 1

    body = default_body()
    if args.body_file:
        body_path = Path(args.body_file).resolve()
        body = body_path.read_text(encoding="utf-8")

    sig_path = Path(args.signature_file).resolve() if args.signature_file else None
    signature = load_signature(sig_path)
    if signature:
        body = body.rstrip() + "\n\n" + signature

    dry_run = not args.send
    if not dry_run and not args.i_understand:
        print(
            "Refusing to send without --i-understand (safety check).",
            file=sys.stderr,
        )
        return 1

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_dir = Path(args.log_dir).resolve()
    log_path = log_dir / f"send-log-{ts}.csv"

    print(f"Recipients (after dedupe/suppression): {len(recipients)}")
    print(f"Mode: {'DRY_RUN' if dry_run else 'SEND'}")
    print(f"Max this run: {args.max_per_run}")
    print(f"Delay: {args.delay:.1f}s")
    print(f"Log: {log_path}")
    print()
    print(f"Subject: {args.subject}")
    print(f"From: {args.from_addr}")
    if args.reply_to:
        print(f"Reply-To: {args.reply_to}")
    print()

    if not recipients:
        print("No recipients to process.")
        return 0

    if dry_run:
        preview_n = min(5, len(recipients))
        print("Preview recipients:")
        for r in recipients[:preview_n]:
            print(f"  - {r}")
        if len(recipients) > preview_n:
            print(f"  ... and {len(recipients) - preview_n} more")
        print()
        print("Body preview (first 25 lines):")
        for i, line in enumerate(body.splitlines()[:25], start=1):
            print(f"{i:02d} {line}")
        print()
        # Log DRY_RUN rows for traceability
        return send_messages(
            smtp=SmtpConfig(host="dry-run", port=0, username="", password="", use_starttls=True),
            from_addr=args.from_addr,
            reply_to=args.reply_to or None,
            recipients=recipients,
            subject=args.subject,
            body=body,
            dry_run=True,
            per_email_delay_s=args.delay,
            max_per_run=args.max_per_run,
            log_path=log_path,
        )

    smtp = get_smtp_config_from_env()
    return send_messages(
        smtp=smtp,
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


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

