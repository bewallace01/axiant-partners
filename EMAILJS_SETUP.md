# EmailJS Setup Instructions

This guide will help you configure EmailJS to receive form submissions via email.

## Step 1: Create an EmailJS Account

1. Go to [https://www.emailjs.com/](https://www.emailjs.com/)
2. Sign up for a free account (free tier allows 200 emails/month)
3. Verify your email address

## Step 2: Add an Email Service

1. In your EmailJS dashboard, go to **Email Services**
2. Click **Add New Service**
3. Choose your email provider (Gmail, Outlook, etc.) or use **Custom SMTP**
4. Follow the setup instructions for your chosen provider
5. Note your **Service ID** (you'll need this later)

## Step 3: Create Email Templates

You need to create two email templates - one for loan applications and one for contact form submissions.

### Template 1: Loan Application Form

1. Go to **Email Templates** in your EmailJS dashboard
2. Click **Create New Template**
3. Name it: "Loan Application"
4. Set the **Subject** to: `New Loan Application - {{reference_number}}`
5. Set the **Content** to:

```
New Loan Application Received

Reference Number: {{reference_number}}

Contact Information:
- Name: {{full_name}}
- Email: {{email}}
- Phone: {{phone}}

Business Information:
- Business Name: {{business_name}}
- Loan Amount: {{loan_amount}}
- Loan Type: {{loan_type}}
- Credit Score: {{credit_score}}
- Annual Revenue: {{revenue}}
- Years in Business: {{years_in_business}}
- Equipment Description: {{equipment_description}}

---
This email was sent from the Axiant Partners website.
```

6. Click **Save**
7. Note your **Template ID** (you'll need this later)

### Template 2: Contact Form

1. Create another template
2. Name it: "Contact Form"
3. Set the **Subject** to: `Contact Form Submission - {{subject}}`
4. Set the **Content** to:

```
New Contact Form Submission

From: {{from_name}}
Email: {{from_email}}
Phone: {{phone}}
Subject: {{subject}}

Message:
{{message}}

---
This email was sent from the Axiant Partners website.
```

5. Click **Save**
6. Note your **Template ID** (you'll need this later)

## Step 4: Get Your Public Key

1. Go to **Account** → **General** in your EmailJS dashboard
2. Find your **Public Key** (also called API Key)
3. Copy this key

## Step 5: Update Your Website Files

You need to replace the placeholder values in your code with your actual EmailJS credentials.

### In `match.html` and `script.js`:

Replace these placeholders:
- `YOUR_PUBLIC_KEY` → Your EmailJS Public Key
- `YOUR_SERVICE_ID` → Your Email Service ID
- `YOUR_TEMPLATE_ID` → Your "Loan Application" Template ID
- `YOUR_EMAIL@example.com` → Your email address where you want to receive applications

### In `contact.html`:

Replace these placeholders:
- `YOUR_PUBLIC_KEY` → Your EmailJS Public Key
- `YOUR_SERVICE_ID` → Your Email Service ID
- `YOUR_TEMPLATE_ID` → Your "Contact Form" Template ID
- `YOUR_EMAIL@example.com` → Your email address where you want to receive contact messages

## Step 6: Test Your Forms

1. Open your website in a browser
2. Fill out and submit the loan application form
3. Fill out and submit the contact form
4. Check your email inbox for the submissions

## Troubleshooting

- **Emails not sending?** Check the browser console (F12) for error messages
- **"EmailJS not loaded" warning?** Make sure the EmailJS script is loading correctly
- **Template variables not working?** Make sure the variable names in your template match exactly what's in the code
- **Rate limiting?** Free tier allows 200 emails/month. Upgrade if you need more.

## Alternative Solutions

If EmailJS doesn't work for your needs, consider:

1. **Formspree** - Another form backend service (similar to EmailJS)
2. **Backend Server** - Set up a Node.js, PHP, or Python server to handle form submissions
3. **Google Forms** - Embed Google Forms (less customizable)

## Security Note

The EmailJS Public Key is safe to expose in client-side code. However, for production use, consider:
- Setting up rate limiting
- Adding CAPTCHA to prevent spam
- Using a backend server for additional security

