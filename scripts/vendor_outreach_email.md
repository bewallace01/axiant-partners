## Quick setup (Alex / Outlook)

1. Copy the example env script and add your password (App Password if MFA is on):
   ```powershell
   Copy-Item .\scripts\load-outlook-email-env.ps1.example .\scripts\load-outlook-email-env.ps1
   notepad .\scripts\load-outlook-email-env.ps1
   ```
   Replace `PASTE_APP_PASSWORD_OR_PASSWORD_HERE` only. The example uses `alex@axiantpartners.com` — change the email lines if your mailbox is different.

**Optional — use your real signature:**  
Copy `scripts/outreach-signature.example.txt` to `scripts/outreach-signature.txt`, paste your usual email signature into it, then in `load-outlook-email-env.ps1` uncomment and set:
`$env:AXIANT_SIGNATURE_FILE = (Join-Path $PSScriptRoot "outreach-signature.txt")`  
Or pass `--signature-file ".\scripts\outreach-signature.txt"` when you run the sender. The script appends the file contents to every email.

2. Each time you open a new PowerShell window in the project:
   ```powershell
   cd "path\to\axiant-partners-main"
   . .\scripts\load-outlook-email-env.ps1
   python .\scripts\send_vendor_outreach.py --input "C:\path\to\recipients.txt"
   ```

`load-outlook-email-env.ps1` is **gitignored** so your password is never committed.

**Alternative — no app password:** You can send the same outreach using **Microsoft Graph (OAuth2)** so no app password is needed. See **[scripts/vendor_outreach_graph.md](vendor_outreach_graph.md)** for app registration and `send_vendor_outreach_graph.py`. Ideal for automation.

---

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

**Outlook / Microsoft 365:**

```powershell
$env:AXIANT_SMTP_HOST="smtp.office365.com"
$env:AXIANT_SMTP_PORT="587"
$env:AXIANT_SMTP_USER="yourname@yourdomain.com"
$env:AXIANT_SMTP_PASS="YOUR_PASSWORD_OR_APP_PASSWORD"
$env:AXIANT_SMTP_STARTTLS="1"

$env:AXIANT_FROM_EMAIL="yourname@yourdomain.com"
$env:AXIANT_REPLY_TO="yourname@yourdomain.com"
```

- Use your **full Outlook/Microsoft 365 email** as the user and from address.
- **Password:** If your account has **multi-factor authentication (MFA)** turned on, you must use an **App Password**, not your normal login password. To create one: Microsoft 365 → Security → Advanced security → App passwords (or sign in at account.microsoft.com/security and create an app password). If you don't have MFA, you can use your normal account password.
- These env vars apply only to the current PowerShell window; repeat them each time you open a new terminal, or set them in your PowerShell profile.

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

Default copy is optimized for embed outreach. To override:

```powershell
python .\scripts\send_vendor_outreach.py --input "C:\Users\alexr\Desktop\recipients.txt" --body-file ".\scripts\outreach-embed-calculator-body.txt"
```

Or edit `scripts/outreach-embed-calculator-body.txt` and point `--body-file` at your version.

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

