# Vendor outreach via Microsoft Graph (no app password)

Use **Microsoft Graph API** with OAuth2 so you can send outreach emails **without an app password**. Ideal for automation (scheduled tasks, scripts, or CI). Same behavior as the SMTP script: dry-run by default, rate limiting, suppression list, body/signature files.

---

## 1. App registration (one-time, as Microsoft 365 admin)

1. **Open Entra (Azure AD)**  
   - Go to [https://entra.microsoft.com](https://entra.microsoft.com) and sign in as an admin.

2. **Create an app**  
   - Left menu: **Identity** → **Applications** → **App registrations** (or **Entra ID** → **App registrations**).  
   - Click **+ New registration**.  
   - **Name:** e.g. `Axiant Outreach Mail Sender`.  
   - **Supported account types:** **Accounts in this organizational directory only**.  
   - **Redirect URI:** leave blank.  
   - Click **Register**.

3. **Copy IDs**  
   - On the app’s **Overview** page, copy:
     - **Application (client) ID**
     - **Directory (tenant) ID**

4. **Create a client secret**  
   - Go to **Certificates & secrets** → **+ New client secret**.  
   - Description: e.g. `Outreach script`.  
   - Expiry: as you prefer (e.g. 24 months).  
   - Click **Add**.  
   - **Copy the secret Value immediately** (it’s shown only once).  
   - You’ll use this as `AXIANT_CLIENT_SECRET`.

5. **Add Graph permission**  
   - Go to **API permissions** → **+ Add a permission**.  
   - **Microsoft Graph** → **Application permissions**.  
   - Search for **Mail.Send**, select it, click **Add permissions**.  
   - Click **Grant admin consent for [your org]** so the permission shows as granted.

6. **Confirm**  
   - Under **API permissions**, you should see **Mail.Send** with **Application** type and **Granted**.

---

## 2. Set environment variables

Use one of these:

**Option A – PowerShell (current session)**  
In the project folder:

```powershell
$env:AXIANT_TENANT_ID    = "YOUR_TENANT_ID"      # Directory (tenant) ID
$env:AXIANT_CLIENT_ID    = "YOUR_CLIENT_ID"      # Application (client) ID
$env:AXIANT_CLIENT_SECRET= "YOUR_CLIENT_SECRET" # Secret value from step 4
$env:AXIANT_FROM_EMAIL   = "alex@axiantpartners.com"
$env:AXIANT_REPLY_TO     = "alex@axiantpartners.com"
# Optional: signature file
$env:AXIANT_SIGNATURE_FILE = (Join-Path $PSScriptRoot "outreach-signature.txt")
```

**Option B – Local env script (recommended for automation)**  
Copy the example and fill in the secret (do not commit the real file):

```powershell
Copy-Item .\scripts\load-outlook-graph-env.ps1.example .\scripts\load-outlook-graph-env.ps1
notepad .\scripts\load-outlook-graph-env.ps1
```

Then in that file set `AXIANT_TENANT_ID`, `AXIANT_CLIENT_ID`, `AXIANT_CLIENT_SECRET`, and `AXIANT_FROM_EMAIL`.  
Before running the script, load env:

```powershell
. .\scripts\load-outlook-graph-env.ps1
```

---

## 3. Install dependency

```powershell
pip install msal
```

Or from the project:

```powershell
pip install -r scripts/requirements-outreach-graph.txt
```

---

## 4. Run the Graph sender

Same CLI as the SMTP script (except it uses Graph under the hood):

**Dry-run (no email sent):**

```powershell
python .\scripts\send_vendor_outreach_graph.py --input ".\scripts\test-recipient.txt"
```

**Send for real:**

```powershell
python .\scripts\send_vendor_outreach_graph.py `
  --input "C:\path\to\recipients.txt" `
  --send --i-understand `
  --max 80 --delay 6
```

Optional: `--body-file`, `--signature-file`, `--subject`, `--suppression`, `--reply-to`, same as the SMTP script.

---

## 5. Automate (e.g. Windows Task Scheduler)

1. Create a task that runs on your schedule (e.g. daily at 9 AM).
2. **Program:** `powershell.exe`  
   **Arguments:**  
   `-NoProfile -ExecutionPolicy Bypass -Command "& { Set-Location 'C:\path\to\axiant-partners-main'; . .\scripts\load-outlook-graph-env.ps1; python .\scripts\send_vendor_outreach_graph.py --input 'C:\path\to\recipients.txt' --send --i-understand --max 80 --delay 6 }"
3. No app password is needed; the task uses the client secret from your env script.

Keep `load-outlook-graph-env.ps1` (and any file containing the secret) out of source control and restrict access to the machine.

---

## Troubleshooting

- **"Missing env: AXIANT_TENANT_ID"** (or CLIENT_ID / CLIENT_SECRET)  
  Load your env script or set those variables in the current session.

- **"Graph token failed"**  
  Check tenant ID, client ID, and client secret. Ensure the secret hasn’t expired and admin consent was granted for **Mail.Send** (Application).

- **403 or "MailboxNotEnabledForRESTAPI"**  
  The account in `AXIANT_FROM_EMAIL` must be a Microsoft 365 mailbox in the same tenant. Shared mailboxes may need different permissions.

- **pip install msal**  
  If you see "No module named 'msal'", run `pip install msal` in the same environment you use to run the script.
