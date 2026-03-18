## Vendor outreach email (Python sender)

This repo includes `scripts/send_vendor_outreach.py`, a small SMTP email sender designed for **controlled outreach**:
- **Dry-run by default** (prints preview + writes a dry-run log)
- **Dedupes recipients**
- **Rate limits** sends with `--delay`
- **Caps** volume with `--max`
- Writes logs under `_analysis/outreach-email/`

### 1) Create your recipients file (recommended)

Create a local file (do **not** commit it) such as:
- `C:\Users\alexr\Desktop\recipients.txt` (one email per line), or
- `C:\Users\alexr\Desktop\recipients.csv` with a column named `email`

### 2) Set SMTP credentials (PowerShell)

Example for Google Workspace / Gmail SMTP (requires an **App Password** if you have 2FA):

```powershell
$env:AXIANT_SMTP_HOST="smtp.gmail.com"
$env:AXIANT_SMTP_PORT="587"
$env:AXIANT_SMTP_USER="YOUR_EMAIL@yourdomain.com"
$env:AXIANT_SMTP_PASS="YOUR_APP_PASSWORD"
$env:AXIANT_SMTP_STARTTLS="1"

$env:AXIANT_FROM_EMAIL="YOUR_EMAIL@yourdomain.com"
$env:AXIANT_REPLY_TO="YOUR_EMAIL@yourdomain.com"
```

For Microsoft 365, your host/port may differ (commonly `smtp.office365.com:587`).

### 3) Dry run (recommended first)

```powershell
python .\scripts\send_vendor_outreach.py --input "C:\Users\alexr\Desktop\recipients.txt"
```

### 4) Send (throttled)

This will send up to 60 emails, waiting 8 seconds between each.

```powershell
python .\scripts\send_vendor_outreach.py `
  --input "C:\Users\alexr\Desktop\recipients.txt" `
  --max 60 `
  --delay 8 `
  --send `
  --i-understand
```

### Optional: Custom body file

Create `body.txt` and pass it in:

```powershell
python .\scripts\send_vendor_outreach.py --input "C:\Users\alexr\Desktop\recipients.txt" --body-file "C:\Users\alexr\Desktop\body.txt"
```

### Optional: Suppression list

To avoid emailing certain addresses (bounces, unsubscribe requests), create a text file with one email per line:

```powershell
python .\scripts\send_vendor_outreach.py `
  --input "C:\Users\alexr\Desktop\recipients.txt" `
  --suppression "C:\Users\alexr\Desktop\suppression.txt"
```

### Notes on deliverability

- Start small (e.g. 30–80/day) and ramp up.
- Avoid sending too fast; use `--delay` (6–12 seconds is a reasonable start).
- Include an opt-out line (the default template includes “reply unsubscribe”).

