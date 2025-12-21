# EmailJS Troubleshooting Guide

If you're not receiving emails, follow these steps:

## Step 1: Check Browser Console

1. Open your website in a browser
2. Press **F12** (or right-click → Inspect) to open Developer Tools
3. Click on the **Console** tab
4. Submit a form
5. Look for any error messages (they'll be in red)

**What to look for:**
- ✅ "EmailJS initialized" - Good! EmailJS loaded correctly
- ✅ "Sending email with data: ..." - Good! Form is submitting
- ✅ "Email sent successfully!" - Good! Email was sent
- ❌ Any red error messages - These tell us what's wrong

## Step 2: Verify EmailJS Configuration

### Check Your EmailJS Dashboard:

1. Go to [https://dashboard.emailjs.com/](https://dashboard.emailjs.com/)
2. Verify your **Service ID**: `service_jweh7na`
3. Verify your **Templates**:
   - Loan Application: `template_dmwg1ey`
   - Contact Form: `template_xujy2ik`

### Check Your Email Service:

1. In EmailJS dashboard, go to **Email Services**
2. Make sure `service_jweh7na` is **Active** and **Connected**
3. If it shows "Not Connected", you need to reconnect it

## Step 3: Verify Template Variables

Your EmailJS templates MUST use these exact variable names:

### Loan Application Template (`template_dmwg1ey`):
```
{{full_name}}
{{email}}
{{phone}}
{{loan_amount}}
{{business_name}}
{{loan_type}}
{{credit_score}}
{{revenue}}
{{years_in_business}}
{{equipment_description}}
{{reference_number}}
{{to_email}}
```

### Contact Form Template (`template_xujy2ik`):
```
{{from_name}}
{{from_email}}
{{phone}}
{{subject}}
{{message}}
{{to_email}}
```

**Important:** Variable names are case-sensitive and must match exactly!

## Step 4: Test EmailJS Directly

1. Go to your EmailJS dashboard
2. Click on **Email Templates**
3. Click on your template (e.g., `template_xujy2ik`)
4. Click **Test** button
5. Fill in test values and send
6. Check if you receive the test email

If the test email works, the issue is with the website code.
If the test email doesn't work, the issue is with your EmailJS configuration.

## Step 5: Common Issues & Solutions

### Issue: "EmailJS is not loaded"
**Solution:** 
- Check your internet connection
- Make sure the EmailJS script is loading (check Network tab in browser console)
- Try clearing browser cache

### Issue: "Email sending failed" with error code 400
**Solution:**
- Template variables don't match
- Check that all variables in your template match the code exactly
- Make sure there are no typos

### Issue: "Email sending failed" with error code 401
**Solution:**
- Public key is incorrect
- Verify your public key: `VCRoHGxbB5ZkCxxUg`
- Check your EmailJS account settings

### Issue: "Email sending failed" with error code 404
**Solution:**
- Service ID or Template ID is incorrect
- Double-check:
  - Service ID: `service_jweh7na`
  - Loan Template: `template_dmwg1ey`
  - Contact Template: `template_xujy2ik`

### Issue: Email sends but goes to spam
**Solution:**
- Check your spam/junk folder
- Add `alex@axiantpartners.com` to your contacts
- Verify your email service is properly configured in EmailJS

### Issue: Free tier limit reached
**Solution:**
- Free tier allows 200 emails/month
- Check your EmailJS dashboard for usage
- Upgrade if needed

## Step 6: Quick Test

Try this in your browser console (F12 → Console tab) after the page loads:

```javascript
// Test EmailJS initialization
if (typeof emailjs !== 'undefined') {
    console.log('EmailJS is loaded');
    emailjs.init("VCRoHGxbB5ZkCxxUg").then(() => {
        console.log('EmailJS initialized successfully');
    });
} else {
    console.error('EmailJS is NOT loaded');
}
```

## Still Not Working?

1. **Check the console errors** - Copy the exact error message
2. **Verify your EmailJS account** - Make sure it's active and not suspended
3. **Test with a simple template** - Create a minimal template with just one variable
4. **Check email service connection** - Make sure your email provider (Gmail, etc.) is connected

## Need More Help?

Share the console error messages and I can help debug further!

