// English-only mode. Language switching intentionally disabled.
(function() {
    'use strict';

    function getPathPrefix() {
        const navLogo = document.querySelector('img.nav-logo');
        if (navLogo) {
            const src = navLogo.getAttribute('src') || '';
            if (src.startsWith('../')) return '../';
        }
        const aboutLink = document.querySelector('.nav-links a[href$="index.html"]');
        if (aboutLink) {
            const href = aboutLink.getAttribute('href') || '';
            if (href.startsWith('../')) return '../';
        }
        return '';
    }

    function ensureServicesMenuLinks() {
        const serviceLinks = [
            { file: 'sba-loans.html', label: 'SBA Loans' },
            { file: 'equipment-financing.html', label: 'Equipment Financing' },
            { file: 'business-line-of-credit.html', label: 'Business Line of Credit' },
            { file: 'working-capital-loans.html', label: 'Working Capital Loans' },
            { file: 'business-term-loans.html', label: 'Business Term Loans' },
            { file: 'commercial-real-estate-loans.html', label: 'Commercial Real Estate Loans' },
            { file: 'commercial-bridge-loans.html', label: 'Commercial Bridge Loans' },
            { file: 'revenue-based-financing.html', label: 'Revenue-Based Financing' },
            { file: 'securities-based-lending.html', label: 'Securities-Based Lending' },
            { file: 'fix-and-flip.html', label: 'Fix and Flip' }
        ];

        document.querySelectorAll('.nav-dropdown-menu').forEach(function(menu) {
            const existing = new Map();
            menu.querySelectorAll('a').forEach(function(link) {
                const href = (link.getAttribute('href') || '').split('#')[0].split('?')[0];
                const file = href.split('/').pop();
                if (!file || existing.has(file)) return;
                existing.set(file, link);
            });

            const firstHref = menu.querySelector('a') ? (menu.querySelector('a').getAttribute('href') || '') : '';
            const prefix = firstHref.startsWith('../') ? '../' : '';

            menu.innerHTML = '';
            serviceLinks.forEach(function(item) {
                const a = document.createElement('a');
                a.setAttribute('href', prefix + item.file);
                a.textContent = item.label;
                menu.appendChild(a);
            });
        });
    }

    function standardizeBrandLogos() {
        const prefix = getPathPrefix();
        document.querySelectorAll('img.nav-logo').forEach(function(img) {
            img.setAttribute('src', prefix + 'logo-horizontal.png');
            img.classList.add('brand-wordmark-logo');
            img.setAttribute('alt', 'Axiant Partners Logo');

            const parent = img.parentElement;
            if (!parent) return;

            // Ensure top-left logo always links back to About page.
            if (parent.tagName.toLowerCase() === 'a') {
                parent.setAttribute('href', prefix + 'index.html');
            } else {
                const link = document.createElement('a');
                link.setAttribute('href', prefix + 'index.html');
                parent.insertBefore(link, img);
                link.appendChild(img);
            }
        });
    }

    function removeWhiteBackgroundFromLogo(img) {
        if (!img || img.dataset.bgRemovedVersion === '4') return;

        function processImage() {
            if (!img.naturalWidth || !img.naturalHeight) return;
            const canvas = document.createElement('canvas');
            canvas.width = img.naturalWidth;
            canvas.height = img.naturalHeight;
            const ctx = canvas.getContext('2d');
            if (!ctx) return;

            ctx.drawImage(img, 0, 0);
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const pixels = imageData.data;

            for (let i = 0; i < pixels.length; i += 4) {
                const r = pixels[i];
                const g = pixels[i + 1];
                const b = pixels[i + 2];
                const a = pixels[i + 3];

                const max = Math.max(r, g, b);
                const min = Math.min(r, g, b);
                const sat = max - min;
                const avg = (r + g + b) / 3;

                // Remove bright neutral background.
                if (avg > 230 && sat < 42) {
                    pixels[i + 3] = 0;
                    continue;
                }

                // Recolor pale fringe pixels to brand blue tones instead of leaving white specks.
                if (avg > 205 && sat < 70) {
                    pixels[i + 3] = Math.max(210, a);
                    pixels[i] = 18;   // deep brand blue
                    pixels[i + 1] = 82;
                    pixels[i + 2] = 148;
                    continue;
                }

                if (avg > 180 && sat < 90) {
                    pixels[i + 3] = Math.max(180, Math.round(a * 0.85));
                    pixels[i] = 46;   // lighter accent blue
                    pixels[i + 1] = 152;
                    pixels[i + 2] = 220;
                }
            }

            ctx.putImageData(imageData, 0, 0);
            img.src = canvas.toDataURL('image/png');
            img.dataset.bgRemovedVersion = '4';
        }

        if (img.complete) {
            processImage();
        } else {
            img.addEventListener('load', processImage, { once: true });
        }
    }

    function cleanAllWordmarkLogos() {
        document.querySelectorAll('img.brand-wordmark-logo, img.nav-logo.hero-center-logo').forEach(function(img) {
            removeWhiteBackgroundFromLogo(img);
        });
    }

    function enhanceGlobalFooter() {
        const footer = document.querySelector('.site-footer');
        if (!footer) return;
        const prefix = getPathPrefix();

        const ctaSection = document.getElementById('globalBottomCta');
        if (!ctaSection) {
            const cta = document.createElement('section');
            cta.id = 'globalBottomCta';
            cta.className = 'global-bottom-cta';
            cta.innerHTML = '' +
                '<div class="global-bottom-cta-inner">' +
                    '<div class="global-bottom-cta-panel">' +
                        '<h2>Ready to Explore Your Financing Options?</h2>' +
                        '<p>Tell us about your financing needs and we will connect you with lender programs that fit your goals.</p>' +
                        '<p class="global-bottom-cta-qualifier"><strong>Typical Baseline Qualifications:</strong></p>' +
                        '<ul class="global-bottom-cta-list">' +
                            '<li>Consistent business revenue</li>' +
                            '<li>Clear funding purpose and timeline</li>' +
                            '<li>U.S.-based business operation</li>' +
                        '</ul>' +
                        '<div class="global-bottom-cta-actions">' +
                            '<a class="btn-primary" href="' + prefix + 'match.html">Apply Now</a>' +
                            '<a class="btn-secondary" href="' + prefix + 'contact.html">Talk to Our Team</a>' +
                        '</div>' +
                    '</div>' +
                '</div>';
            footer.parentNode.insertBefore(cta, footer);
        }

        footer.classList.add('site-footer-enhanced');
        footer.innerHTML = '' +
            '<div class="site-footer-wrap">' +
                '<div class="footer-top">' +
                    '<div class="footer-brand">' +
                        '<div class="footer-brand-mark">' +
                            '<img class="brand-wordmark-logo" src="' + prefix + 'logo-horizontal.png" alt="Axiant Partners Logo">' +
                        '</div>' +
                        '<p>Your resource for business financing and advisory support. We help established businesses find better lender matches and funding structures.</p>' +
                        '<a class="footer-email" href="mailto:alex@axiantpartners.com">alex@axiantpartners.com</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Resources</h4>' +
                        '<a href="' + prefix + 'match.html">Get Started</a>' +
                        '<a href="' + prefix + 'services.html">All Services</a>' +
                        '<a href="' + prefix + 'calculator.html">Loan Calculator</a>' +
                        '<a href="' + prefix + 'blog.html">All Articles</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Financing Guides</h4>' +
                        '<a href="' + prefix + 'sba-loans.html">SBA Loans</a>' +
                        '<a href="' + prefix + 'equipment-financing.html">Equipment Financing</a>' +
                        '<a href="' + prefix + 'business-line-of-credit.html">Line of Credit</a>' +
                        '<a href="' + prefix + 'working-capital-loans.html">Working Capital</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Company</h4>' +
                        '<a href="' + prefix + 'index.html">About Us</a>' +
                        '<a href="' + prefix + 'contact.html">Contact</a>' +
                        '<a href="' + prefix + 'faq.html">FAQ</a>' +
                        '<a href="' + prefix + 'vendors.html">Vendors</a>' +
                    '</div>' +
                '</div>' +
                '<div class="footer-bottom">' +
                    '<p>&copy; 2026 Axiant Partners. All rights reserved.</p>' +
                    '<div class="footer-legal">' +
                        '<a href="' + prefix + 'privacy-policy.html">Privacy Policy</a>' +
                        '<a href="' + prefix + 'terms-and-conditions.html">Terms of Service</a>' +
                        '<a href="' + prefix + 'sitemap.xml">Sitemap</a>' +
                    '</div>' +
                '</div>' +
            '</div>';
    }

    function forceEnglish() {
        document.documentElement.setAttribute('lang', 'en');
        document.documentElement.setAttribute('dir', 'ltr');
        localStorage.setItem('language', 'en');

        // Remove any existing selector if injected by older builds/cache.
        const selector = document.getElementById('languageSelector');
        if (selector && selector.parentElement) {
            const wrapper = selector.closest('.language-selector-wrapper');
            if (wrapper) {
                wrapper.remove();
            } else {
                selector.remove();
            }
        }

        // Keep full service tabs visible without translation script logic.
        ensureServicesMenuLinks();
        standardizeBrandLogos();
        enhanceGlobalFooter();
        cleanAllWordmarkLogos();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', forceEnglish);
    } else {
        forceEnglish();
    }

    // Keep a harmless stub in case any legacy code references this object.
    window.languageSwitcher = {
        setLanguage: function() {
            forceEnglish();
        },
        getLanguage: function() {
            return 'en';
        },
        translatePage: function() {
            forceEnglish();
        }
    };
})();
