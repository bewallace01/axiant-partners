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

            // Resolve links from current page depth (critical for /blog/* pages).
            let prefix = getPathPrefix();
            if (!prefix) {
                const path = window.location.pathname || '';
                if (path.indexOf('/blog/') !== -1 || path.indexOf('\\blog\\') !== -1) {
                    prefix = '../';
                }
            }

            menu.innerHTML = '';
            serviceLinks.forEach(function(item) {
                const a = document.createElement('a');
                a.setAttribute('href', prefix + item.file);
                a.textContent = item.label;
                menu.appendChild(a);
            });
        });
    }

    function enhanceMobileMenuBehavior() {
        const nav = document.querySelector('.main-nav');
        const menuToggle = document.querySelector('.mobile-menu-toggle');
        const navLinks = document.querySelector('.nav-links');
        if (!nav || !menuToggle || !navLinks || nav.dataset.mobileMenuEnhanced === '1') return;

        nav.dataset.mobileMenuEnhanced = '1';

        let overlay = document.querySelector('.mobile-menu-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'mobile-menu-overlay';
            document.body.appendChild(overlay);
        }

        const mobileQuery = window.matchMedia('(max-width: 768px)');

        function closeMenu() {
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.classList.remove('mobile-nav-open');
            nav.querySelectorAll('.nav-dropdown').forEach(function(dropdown) {
                dropdown.classList.remove('mobile-open');
                const trigger = dropdown.querySelector('.nav-dropdown-trigger');
                if (trigger) trigger.setAttribute('aria-expanded', 'false');
            });
        }

        function syncMenuStateFromClasses() {
            if (mobileQuery.matches && navLinks.classList.contains('active')) {
                document.body.classList.add('mobile-nav-open');
            } else {
                document.body.classList.remove('mobile-nav-open');
            }
        }

        menuToggle.addEventListener('click', function() {
            window.setTimeout(syncMenuStateFromClasses, 0);
        });

        overlay.addEventListener('click', closeMenu);

        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') closeMenu();
        });

        window.addEventListener('resize', function() {
            if (!mobileQuery.matches) closeMenu();
        });

        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                closeMenu();
            });
        });

        nav.querySelectorAll('.nav-dropdown').forEach(function(dropdown) {
            const trigger = dropdown.querySelector('.nav-dropdown-trigger');
            if (!trigger) return;
            trigger.setAttribute('aria-expanded', 'false');

            trigger.addEventListener('click', function(event) {
                if (!mobileQuery.matches) return;
                event.preventDefault();

                const willOpen = !dropdown.classList.contains('mobile-open');
                nav.querySelectorAll('.nav-dropdown').forEach(function(other) {
                    other.classList.remove('mobile-open');
                    const otherTrigger = other.querySelector('.nav-dropdown-trigger');
                    if (otherTrigger) otherTrigger.setAttribute('aria-expanded', 'false');
                });

                if (willOpen) {
                    dropdown.classList.add('mobile-open');
                    trigger.setAttribute('aria-expanded', 'true');
                }
            });
        });
    }

    function standardizeBrandLogos() {
        const prefix = getPathPrefix();
        document.querySelectorAll('img.nav-logo').forEach(function(img) {
            img.setAttribute('src', prefix + 'logo-horizontal-transparent.png');
            img.classList.add('brand-wordmark-logo');
            img.setAttribute('alt', 'Axiant Partners Logo');
            img.addEventListener('error', function onLogoError() {
                img.removeEventListener('error', onLogoError);
                img.setAttribute('src', prefix + 'logo-horizontal.png');
            });

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
        const src = (img && img.getAttribute('src')) || '';
        if (src.indexOf('logo-horizontal-transparent.png') !== -1) return;
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
        if (document.querySelector('img.brand-wordmark-logo[src*="logo-horizontal-transparent.png"]')) return;
        document.querySelectorAll('img.brand-wordmark-logo, img.nav-logo.hero-center-logo').forEach(function(img) {
            removeWhiteBackgroundFromLogo(img);
        });
    }

    function enhanceGlobalFooter() {
        const footer = document.querySelector('.site-footer');
        if (!footer) return;
        const prefix = getPathPrefix();
        const currentYear = new Date().getFullYear();

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
                    '<p>&copy; ' + currentYear + ' Axiant Partners. All rights reserved.</p>' +
                    '<div class="footer-legal">' +
                        '<a href="' + prefix + 'privacy-policy.html">Privacy Policy</a>' +
                        '<a href="' + prefix + 'terms-and-conditions.html">Terms of Service</a>' +
                        '<a href="' + prefix + 'sitemap.xml">Sitemap</a>' +
                    '</div>' +
                '</div>' +
            '</div>';
    }

    function syncLegacyFooterYear() {
        const currentYear = new Date().getFullYear();
        document.querySelectorAll('.site-footer p').forEach(function(node) {
            if (!node || !node.textContent) return;
            node.textContent = node.textContent.replace(/\u00A9\s*20\d{2}\s+Axiant Partners/gi, '\u00A9 ' + currentYear + ' Axiant Partners');
        });
    }

    function slugifyHeading(text) {
        return String(text || '')
            .toLowerCase()
            .trim()
            .replace(/[^a-z0-9\s-]/g, '')
            .replace(/\s+/g, '-')
            .replace(/-+/g, '-')
            .replace(/^-|-$/g, '');
    }

    function enhanceBlogPostLayout() {
        const container = document.querySelector('.form-container.blog-post-content');
        if (!container || container.dataset.blogEnhanced === '1') return;

        const allChildren = Array.from(container.children);
        const contentStartIdx = allChildren.findIndex(function(node) {
            return node.tagName && node.tagName.toLowerCase() === 'h2';
        });
        if (contentStartIdx < 0) return;

        container.dataset.blogEnhanced = '1';
        const prefix = getPathPrefix();
        const introNodes = allChildren.slice(0, contentStartIdx);
        const articleNodes = allChildren.slice(contentStartIdx);

        const shell = document.createElement('div');
        shell.className = 'blog-post-shell';

        const main = document.createElement('article');
        main.className = 'blog-post-main';

        const rail = document.createElement('aside');
        rail.className = 'blog-post-rail';

        const tocList = document.createElement('ul');
        tocList.className = 'blog-post-toc-list';

        let sectionCounter = 0;
        let currentSection = null;
        articleNodes.forEach(function(node) {
            const tag = node.tagName ? node.tagName.toLowerCase() : '';
            if (tag === 'h2') {
                sectionCounter += 1;
                const base = slugifyHeading(node.textContent) || ('section-' + sectionCounter);
                const id = 'section-' + sectionCounter + '-' + base;
                node.id = id;

                const tocItem = document.createElement('li');
                const tocLink = document.createElement('a');
                tocLink.href = '#' + id;
                tocLink.textContent = node.textContent.trim();
                tocItem.appendChild(tocLink);
                tocList.appendChild(tocItem);

                currentSection = document.createElement('section');
                currentSection.className = 'blog-article-block';
                currentSection.appendChild(node);
                main.appendChild(currentSection);
                return;
            }

            if (!currentSection) {
                currentSection = document.createElement('section');
                currentSection.className = 'blog-article-block';
                main.appendChild(currentSection);
            }
            currentSection.appendChild(node);
        });

        const totalWords = container.textContent.trim().split(/\s+/).filter(Boolean).length;
        const readMinutes = Math.max(3, Math.round(totalWords / 220));

        rail.innerHTML = '' +
            '<div class="blog-rail-card blog-rail-meta">' +
                '<h3>Article Guide</h3>' +
                '<p>Estimated read: <strong>' + readMinutes + ' min</strong></p>' +
            '</div>';

        if (tocList.children.length) {
            const tocCard = document.createElement('div');
            tocCard.className = 'blog-rail-card blog-rail-toc';
            const title = document.createElement('h3');
            title.textContent = 'On This Page';
            tocCard.appendChild(title);
            tocCard.appendChild(tocList);
            rail.appendChild(tocCard);
        }

        // Use explicit offset scrolling so section headings never hide behind sticky nav.
        tocList.querySelectorAll('a[href^="#"]').forEach(function(link) {
            link.addEventListener('click', function(event) {
                const href = link.getAttribute('href');
                if (!href || href.length < 2) return;
                const target = document.getElementById(href.slice(1));
                if (!target) return;

                event.preventDefault();
                const nav = document.querySelector('.main-nav');
                const navHeight = nav ? nav.getBoundingClientRect().height : 88;
                const extraOffset = window.matchMedia('(max-width: 768px)').matches ? 18 : 22;
                const y = target.getBoundingClientRect().top + window.pageYOffset - navHeight - extraOffset;

                window.scrollTo({
                    top: Math.max(0, y),
                    behavior: 'smooth'
                });
            });
        });

        shell.appendChild(main);
        shell.appendChild(rail);

        container.innerHTML = '';
        introNodes.forEach(function(node) { container.appendChild(node); });
        container.appendChild(shell);
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
        enhanceMobileMenuBehavior();
        standardizeBrandLogos();
        syncLegacyFooterYear();
        enhanceGlobalFooter();

        // Defer non-critical visual enhancements until browser is idle.
        const runDeferred = function() {
            enhanceBlogPostLayout();
            cleanAllWordmarkLogos();
        };
        if (window.requestIdleCallback) {
            window.requestIdleCallback(runDeferred, { timeout: 1500 });
        } else {
            window.setTimeout(runDeferred, 180);
        }
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
