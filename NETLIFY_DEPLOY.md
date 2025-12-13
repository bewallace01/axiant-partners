# Deploy to Netlify - Step by Step Guide

## Quick Start (5 minutes)

### Method 1: Drag & Drop (Easiest)

1. **Go to Netlify**
   - Visit [app.netlify.com](https://app.netlify.com)
   - Sign up for a free account (or log in if you have one)
   - You can sign up with:
     - Email
     - GitHub account
     - Google account

2. **Deploy Your Site**
   - Once logged in, you'll see the Netlify dashboard
   - Look for the area that says "Want to deploy a new site without connecting to Git? Drag and drop your site output folder here"
   - **Drag your entire "Axiant Partners" folder** onto that area
   - Wait 10-30 seconds for deployment

3. **Get Your URL**
   - Netlify will automatically generate a URL like: `random-name-12345.netlify.app`
   - Your site is now live! 🎉

4. **Customize Your Site Name** (Optional)
   - Click "Site settings" in the top menu
   - Click "Change site name"
   - Enter something like: `axiant-partners` or `axiant-loans`
   - Your new URL will be: `axiant-partners.netlify.app`

### Method 2: Using Netlify Drop (Alternative)

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop your "Axiant Partners" folder
3. Get your live URL instantly

## After Deployment

### 1. Test Your Site
- Click on your site URL to open it
- Test all pages:
  - Homepage (index.html)
  - Find Match (match.html)
  - FAQ (faq.html)
  - Contact (contact.html)
  - Privacy Policy
  - Terms and Conditions
- Test the form submission
- Test on mobile (use your phone browser)

### 2. Update Meta Tags (Important!)

After you get your Netlify URL, update the meta tags in `index.html`:

1. Open `index.html` in your code editor
2. Find lines 12-20 (the Open Graph meta tags)
3. Replace `https://axiantpartners.com/` with your actual Netlify URL
4. For example, if your URL is `axiant-partners.netlify.app`, change:
   - `content="https://axiantpartners.com/"` to `content="https://axiant-partners.netlify.app/"`
   - `content="https://axiantpartners.com/logo.jpg"` to `content="https://axiant-partners.netlify.app/logo.jpg"`
5. Re-upload the updated `index.html` to Netlify (drag and drop again, or use Git if you set it up)

### 3. Set Up Custom Domain (Optional - Later)

If you want a custom domain like `axiantpartners.com`:

1. In Netlify dashboard, go to "Domain settings"
2. Click "Add custom domain"
3. Enter your domain name
4. Follow Netlify's instructions to update your DNS settings
5. Wait for DNS propagation (can take a few hours)

## Files to Upload

Make sure these files are in your folder when you drag to Netlify:
- ✅ index.html
- ✅ match.html
- ✅ faq.html
- ✅ contact.html
- ✅ privacy-policy.html
- ✅ terms-and-conditions.html
- ✅ styles.css
- ✅ script.js
- ✅ logo.jpg
- ✅ netlify.toml (optional, but recommended)
- ✅ Axiant_PrivacyPolicy_UPDATED.pdf (if you still want it)
- ✅ Axiant_TermsAndConditions_UPDATED.pdf (if you still want it)

## Troubleshooting

### Site Not Loading?
- Check that `index.html` is in the root folder
- Make sure all file names match exactly (case-sensitive)
- Check Netlify deploy logs for errors

### Images Not Showing?
- Make sure `logo.jpg` is in the same folder as your HTML files
- Check that image paths in HTML match file names exactly

### Form Not Working?
- The form will work for collecting data, but submissions won't be saved without a backend
- Consider adding Netlify Forms (see below) or connecting to a form service

## Advanced: Netlify Forms (Optional)

To collect form submissions:

1. Add `netlify` attribute to your form in `match.html`:
   ```html
   <form id="loanApplicationForm" netlify>
   ```

2. Add a hidden input:
   ```html
   <input type="hidden" name="form-name" value="loanApplicationForm">
   ```

3. Redeploy your site
4. Submissions will appear in Netlify dashboard under "Forms"

## Need Help?

- **Netlify Docs**: https://docs.netlify.com
- **Netlify Support**: https://www.netlify.com/support/
- **Community Forum**: https://answers.netlify.com

## Next Steps

1. ✅ Deploy to Netlify (drag & drop)
2. ✅ Test your live site
3. ✅ Update meta tags with your Netlify URL
4. ✅ Share your website URL!
5. ⏭️ (Optional) Set up custom domain later

Your website will be live and shareable in minutes! 🚀

