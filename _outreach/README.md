# Outreach Email Workflow

Store your recipient list here. The script tracks who you've emailed so you never send twice.

## Files

| File | Purpose |
|------|---------|
| `recipients.txt` | Master list of emails to contact. One per line. Add lines starting with `#` for comments. |
| `sent.txt` | **Auto-updated** — Emails you've already sent to. The script appends to this after each run. Don't edit by hand. |
| `do-not-email.txt` | Unsubscribes, bounces, "stop" requests. Add addresses here; use `--suppression` so they're never emailed. |

## How it works

1. **Put your emails** in `recipients.txt` (one per line).
2. **Run the script** with `--sent-file`:
   ```powershell
   . .\scripts\load-outlook-graph-env.ps1
   python .\scripts\send_vendor_outreach_graph.py `
   --input ".\_outreach\recipients.txt" `
   --sent-file ".\_outreach\sent.txt" `
   --suppression ".\_outreach\do-not-email.txt" `
     --send --i-understand `
     --max 60 --delay 8
   ```
3. **Each run** sends to the next batch (skipping anyone already in `sent.txt`), then appends newly sent addresses to `sent.txt`.

## Unsubscribes / do-not-email

When someone replies "unsubscribe" or "stop," add their email to `do-not-email.txt` (one per line). Include `--suppression` in your run command so they're never emailed again.
