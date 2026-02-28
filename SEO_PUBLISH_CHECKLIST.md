# SEO Publish Checklist (Daily)

Use this before publishing each new blog post.

## Per-Post Checklist (Required)

- [ ] URL slug is short, readable, and keyword-aligned (`blog/your-topic.html`)
- [ ] One `H1` only; includes primary keyword naturally
- [ ] Title tag is unique and ~45-65 characters
- [ ] Meta description is unique and ~120-155 characters
- [ ] `og:title` and `twitter:title` match the page title
- [ ] `og:description` and `twitter:description` match meta description
- [ ] Canonical URL points to the correct final page URL
- [ ] Intro paragraph includes target keyword naturally
- [ ] At least one in-body link to the related service page
- [ ] At least one in-body link to a related article
- [ ] At least one in-body link to the topic blog hub
- [ ] `Related Resources` block exists above CTA
- [ ] CTA button text is clear and links to `../match.html`
- [ ] No broken characters/encoding artifacts (no random symbols/letters)
- [ ] All internal links are relative and working locally

## Daily QA (5-10 mins)

- [ ] Open new post in browser and test all links
- [ ] Confirm Services dropdown links work from the new post
- [ ] Verify theme toggle/mobile nav still function
- [ ] Validate no console errors on post page
- [ ] Add at least 1 link from an older related article to the new post

## Weekly SEO Maintenance (30-45 mins)

- [ ] Update 5-10 older posts with links to newest posts
- [ ] Refresh top-performing posts (tighten title/description if needed)
- [ ] Check for pages missing Twitter/OG tags
- [ ] Check for duplicate meta titles/descriptions

## Monthly Growth Tasks (60-90 mins)

- [ ] Review Google Search Console queries/pages for opportunities
- [ ] Expand posts that rank on page 2-3 with deeper sections/FAQs
- [ ] Add internal links from high-traffic pages to conversion pages
- [ ] Improve CTR for low-CTR high-impression pages (title/description tests)

## Fast Prompt You Can Reuse With Me

```txt
Run SEO publish checklist on this new post:
<paste post URL/path + template fields>.

Please:
1) validate all metadata and internal links,
2) add/repair related-resources block,
3) confirm encoding is clean,
4) report anything that can hurt rankings.
```

## Automation Command (Optional, Recommended)

Run this after creating a new post file:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts/auto_blog_seo.ps1" -PostPath "blog/your-new-post.html"
```

Run this to refresh all blog articles at once:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts/auto_blog_seo.ps1" -All
```
