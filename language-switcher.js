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

    function enforceAssetVersioning() {
        const version = '20260352';
        document.querySelectorAll('link[rel="stylesheet"]').forEach(function(link) {
            const href = link.getAttribute('href') || '';
            if (!href || href.indexOf('styles.css') === -1) return;
            const clean = href.split('?')[0];
            if (!clean.endsWith('styles.css')) return;
            const next = clean + '?v=' + version;
            if (href !== next) link.setAttribute('href', next);
        });

        document.querySelectorAll('script[src]').forEach(function(script) {
            const src = script.getAttribute('src') || '';
            if (!src) return;
            const clean = src.split('?')[0];
            if (!clean.endsWith('script.js') && !clean.endsWith('language-switcher.js')) return;
            const next = clean + '?v=' + version;
            if (src !== next) script.setAttribute('src', next);
        });
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

        var servicesDropdown = document.querySelector('.nav-links .nav-dropdown');
        var menu = servicesDropdown ? servicesDropdown.querySelector('.nav-dropdown-menu') : null;
        if (!menu) return;

        menu.innerHTML = '';
        serviceLinks.forEach(function(item) {
            var a = document.createElement('a');
            a.setAttribute('href', '/' + item.file);
            a.textContent = item.label;
            menu.appendChild(a);
        });
    }

    function ensureIndustriesMenuLinks() {
        var industryLinks = [
            { file: 'construction-business-financing.html', label: 'Construction' },
            { file: 'trucking-business-financing.html', label: 'Trucking' }
        ];

        var navLinks = document.querySelector('.nav-links');
        if (!navLinks) return;

        var dropdowns = navLinks.querySelectorAll('.nav-dropdown');
        var servicesDropdown = dropdowns[0];
        var industriesDropdown = dropdowns[1];

        if (!industriesDropdown) {
            industriesDropdown = document.createElement('div');
            industriesDropdown.className = 'nav-dropdown';
            industriesDropdown.innerHTML = '<button type="button" class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">Industries</button><div class="nav-dropdown-menu"></div>';
            if (servicesDropdown && servicesDropdown.nextSibling) {
                navLinks.insertBefore(industriesDropdown, servicesDropdown.nextSibling);
            } else {
                navLinks.appendChild(industriesDropdown);
            }
        }

        var menu = industriesDropdown.querySelector('.nav-dropdown-menu');
        if (!menu) return;

        menu.innerHTML = '';
        industryLinks.forEach(function(item) {
            var a = document.createElement('a');
            a.setAttribute('href', '/' + item.file);
            a.textContent = item.label;
            menu.appendChild(a);
        });
    }

    function normalizeServiceMenuLinks() {
        document.querySelectorAll('.nav-dropdown-menu a').forEach(function(link) {
            const href = link.getAttribute('href') || '';
            if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
                return;
            }
            if (href.startsWith('/')) return;
            const file = href.split('?')[0].split('#')[0].split('/').pop();
            if (!file || !file.endsWith('.html')) return;
            link.setAttribute('href', '/' + file);
        });
    }

    function ensureReferralTab() {
        const onReferralPage = /\/referral\.html$/i.test(window.location.pathname || '');
        const navLinksList = document.querySelectorAll('.nav-links');

        // Remove duplicate Referral links (keep only the first)
        const allReferralLinks = Array.from(document.querySelectorAll('.nav-links a[href$="referral.html"]'));
        allReferralLinks.slice(1).forEach(function(link) { link.remove(); });

        // Only add Referral to the first nav-links to avoid duplicates on pages with multiple navs
        const primaryNav = navLinksList[0];
        if (!primaryNav) return;

        let referralLink = primaryNav.querySelector('a[href$="referral.html"]');
        if (!referralLink) {
            referralLink = document.createElement('a');
            referralLink.setAttribute('href', '/referral.html');
            referralLink.textContent = 'Referral';
        }

        if (onReferralPage) {
            referralLink.classList.add('active');
        } else {
            referralLink.classList.remove('active');
        }

        const contactLink = primaryNav.querySelector('a[href$="contact.html"]');
        if (contactLink && contactLink.parentElement === primaryNav) {
            if (contactLink.nextSibling !== referralLink) {
                contactLink.insertAdjacentElement('afterend', referralLink);
            }
        } else {
            const themeToggle = primaryNav.querySelector('.theme-toggle');
            if (themeToggle) {
                primaryNav.insertBefore(referralLink, themeToggle);
            } else {
                primaryNav.appendChild(referralLink);
            }
        }
    }

    function placeThemeToggleInMobileHeader() {
        const nav = document.querySelector('.main-nav');
        const navLinks = document.querySelector('.nav-links');
        const menuToggle = document.querySelector('.mobile-menu-toggle');
        if (!nav || !navLinks || !menuToggle) return;

        // If a previous build left the base toggle in the header, move it back into the menu list.
        const misplacedBaseToggle = nav.querySelector('.theme-toggle:not(.theme-toggle-mobile)');
        if (misplacedBaseToggle && misplacedBaseToggle.parentElement === nav) {
            navLinks.appendChild(misplacedBaseToggle);
        }

        let mobileToggle = nav.querySelector('#themeToggleMobile');
        if (!mobileToggle) {
            mobileToggle = document.createElement('button');
            mobileToggle.className = 'theme-toggle theme-toggle-mobile';
            mobileToggle.id = 'themeToggleMobile';
            mobileToggle.setAttribute('type', 'button');
            mobileToggle.setAttribute('aria-label', 'Toggle dark mode');
            menuToggle.insertAdjacentElement('afterend', mobileToggle);
        }
    }

    function injectMobileHardFixStyles() {
        const style = document.getElementById('mobileHardFixStyles');
        if (style) style.remove();
    }

    function syncNavLogosForTheme(theme) {
        const lightLogos = document.querySelectorAll('.nav-logo-light');
        const darkLogos = document.querySelectorAll('.nav-logo-dark');
        const isDark = theme === 'dark';
        // Keep logo dimensions CSS-driven so dark/light always stay the same size.
        lightLogos.forEach(function(el) {
            el.style.removeProperty('width');
            el.style.removeProperty('height');
            el.style.removeProperty('min-width');
            el.style.removeProperty('max-width');
        });
        darkLogos.forEach(function(el) {
            el.style.removeProperty('width');
            el.style.removeProperty('height');
            el.style.removeProperty('min-width');
            el.style.removeProperty('max-width');
        });

        if (isDark && lightLogos.length && darkLogos.length) {
            /* Force dark logo to load cropped image (cache-bust) */
            darkLogos.forEach(function(el) {
                var src = el.getAttribute('src') || '';
                if (src && src.indexOf('Axiant_light_logo') !== -1 && src.indexOf('v=') === -1) {
                    el.setAttribute('src', src.replace(/\?.*$/, '') + '?v=3');
                }
            });
        }

        lightLogos.forEach(function(el) {
            el.style.setProperty('display', isDark ? 'none' : 'block', 'important');
            el.style.setProperty('visibility', isDark ? 'hidden' : 'visible', 'important');
        });
        darkLogos.forEach(function(el) {
            el.style.setProperty('display', isDark ? 'block' : 'none', 'important');
            el.style.setProperty('visibility', isDark ? 'visible' : 'hidden', 'important');
        });
    }

    function enhanceThemeToggle() {
        const root = document.documentElement;
        const savedTheme = localStorage.getItem('theme');
        root.setAttribute('data-theme', savedTheme === 'dark' ? 'dark' : 'light');

        syncNavLogosForTheme(root.getAttribute('data-theme'));

        const toggles = Array.from(document.querySelectorAll('.theme-toggle'));
        if (!toggles.length) return;

        const syncPressedState = function(theme) {
            toggles.forEach(function(toggle) {
                toggle.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
            });
        };

        syncPressedState(root.getAttribute('data-theme'));
        toggles.forEach(function(toggle) {
            if (!toggle || toggle.dataset.themeEnhanced === '1') return;
            toggle.dataset.themeEnhanced = '1';
            toggle.addEventListener('click', function(event) {
                event.preventDefault();
                event.stopPropagation();
                const nextTheme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                root.setAttribute('data-theme', nextTheme);
                localStorage.setItem('theme', nextTheme);
                syncPressedState(nextTheme);
                syncNavLogosForTheme(nextTheme);
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

        const topbar = navLinks.querySelector('.mobile-menu-topbar');
        if (topbar) {
            topbar.remove();
        }

        function openMenu() {
            if (!mobileQuery.matches) return;
            menuToggle.classList.add('active');
            navLinks.classList.add('active');
            document.body.classList.add('mobile-nav-open');
            overlay.style.pointerEvents = 'auto';
            menuToggle.setAttribute('aria-expanded', 'true');
        }

        function closeMenu() {
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.classList.remove('mobile-nav-open');
            overlay.style.pointerEvents = 'none';
            menuToggle.setAttribute('aria-expanded', 'false');
            nav.querySelectorAll('.nav-dropdown').forEach(function(dropdown) {
                dropdown.classList.remove('mobile-open');
                const trigger = dropdown.querySelector('.nav-dropdown-trigger');
                if (trigger) trigger.setAttribute('aria-expanded', 'false');
            });
        }

        menuToggle.setAttribute('aria-expanded', 'false');
        overlay.style.pointerEvents = 'none';
        menuToggle.addEventListener('click', function(event) {
            if (!mobileQuery.matches) return;
            event.preventDefault();
            event.stopPropagation();
            if (navLinks.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        overlay.addEventListener('click', closeMenu);
        navLinks.addEventListener('click', function(event) {
            event.stopPropagation();
        });

        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') closeMenu();
        });

        document.addEventListener('click', function(event) {
            if (!mobileQuery.matches || !navLinks.classList.contains('active')) return;
            if (!event.target.closest('.main-nav')) closeMenu();
        });

        window.addEventListener('resize', function() {
            if (!mobileQuery.matches) closeMenu();
        });

        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                window.setTimeout(closeMenu, 0);
            });
        });

        nav.querySelectorAll('.nav-dropdown').forEach(function(dropdown) {
            const trigger = dropdown.querySelector('.nav-dropdown-trigger');
            if (!trigger) return;
            trigger.setAttribute('aria-expanded', 'false');

            trigger.addEventListener('click', function(event) {
                if (!mobileQuery.matches) return;
                event.preventDefault();
                event.stopPropagation();

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
        document.querySelectorAll('img.nav-logo').forEach(function(img) {
            // Skip theme-aware nav logos (light/dark mode swap); do not overwrite their src.
            if (img.classList.contains('nav-logo-light') || img.classList.contains('nav-logo-dark')) return;

            img.setAttribute('src', '/logo-horizontal-transparent.png');
            img.classList.add('brand-wordmark-logo');
            img.setAttribute('alt', 'Axiant Partners Logo');
            img.addEventListener('error', function onLogoError() {
                img.removeEventListener('error', onLogoError);
                img.setAttribute('src', '/logo-horizontal.png');
            });

            const parent = img.parentElement;
            if (!parent) return;

            // Ensure top-left logo always links back to About page.
            if (parent.tagName.toLowerCase() === 'a') {
                parent.setAttribute('href', '/');
            } else {
                const link = document.createElement('a');
                link.setAttribute('href', '/');
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
                            '<a class="btn-primary" href="/match.html">Apply Now</a>' +
                            '<a class="btn-secondary" href="/contact.html">Talk to Our Team</a>' +
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
                            '<img class="brand-wordmark-logo" src="/logo-horizontal.png" alt="Axiant Partners Logo">' +
                        '</div>' +
                        '<p>Your resource for business financing and advisory support. We help established businesses find better lender matches and funding structures.</p>' +
                        '<a class="footer-email" href="mailto:alex@axiantpartners.com">alex@axiantpartners.com</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Resources</h4>' +
                        '<a href="/match.html">Get Started</a>' +
                        '<a href="/services.html">All Services</a>' +
                        '<a href="/calculator.html">Loan Calculator</a>' +
                        '<a href="/blog.html">All Articles</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Financing Guides</h4>' +
                        '<a href="/sba-loans.html">SBA Loans</a>' +
                        '<a href="/equipment-financing.html">Equipment Financing</a>' +
                        '<a href="/business-line-of-credit.html">Line of Credit</a>' +
                        '<a href="/working-capital-loans.html">Working Capital</a>' +
                        '<a href="/business-term-loans.html">Business Term Loans</a>' +
                        '<a href="/commercial-real-estate-loans.html">Commercial Real Estate</a>' +
                        '<a href="/commercial-bridge-loans.html">Commercial Bridge Loans</a>' +
                        '<a href="/revenue-based-financing.html">Revenue-Based Financing</a>' +
                        '<a href="/securities-based-lending.html">Securities-Based Lending</a>' +
                        '<a href="/fix-and-flip.html">Fix and Flip</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Industries</h4>' +
                        '<a href="/construction-business-financing.html">Construction</a>' +
                        '<a href="/trucking-business-financing.html">Trucking</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Company</h4>' +
                        '<a href="/">About Us</a>' +
                        '<a href="/contact.html">Contact</a>' +
                        '<a href="/faq.html">FAQ</a>' +
                        '<a href="/vendors.html">Vendors</a>' +
                        '<div class="footer-social">' +
                            '<h4>Follow Us</h4>' +
                            '<a href="https://www.linkedin.com/company/axiantpartners/" target="_blank" rel="noopener noreferrer">LinkedIn</a>' +
                            '<a href="https://www.facebook.com/share/1j27PpAoUS/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer">Facebook</a>' +
                            '<a href="https://www.instagram.com/axiantpartners?igsh=a25pcmZ3NGpxb3Fl&utm_source=qr" target="_blank" rel="noopener noreferrer">Instagram</a>' +
                            '<a href="https://www.youtube.com/@axeltheloanlion" target="_blank" rel="noopener noreferrer">YouTube</a>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
                '<div class="footer-bottom">' +
                    '<p>&copy; ' + currentYear + ' Axiant Partners. All rights reserved.</p>' +
                    '<div class="footer-legal">' +
                        '<a href="/privacy-policy.html">Privacy Policy</a>' +
                        '<a href="/terms-and-conditions.html">Terms of Service</a>' +
                        '<a href="/sitemap.xml">Sitemap</a>' +
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

    function injectAxelChatbot() {
        if (document.getElementById('axelChatLauncher')) return;
        const autoOpenKey = 'axelChatAutoOpenedV1';

        const launcher = document.createElement('button');
        launcher.id = 'axelChatLauncher';
        launcher.className = 'axel-chat-launcher';
        launcher.setAttribute('type', 'button');
        launcher.setAttribute('aria-label', 'Open Axel AI chat assistant');
        launcher.innerHTML = '<span class="axel-chat-launcher-icon">🦁</span><span class="axel-chat-launcher-text">Chat with Axel</span>';

        const panel = document.createElement('section');
        panel.id = 'axelChatPanel';
        panel.className = 'axel-chat-panel';
        panel.setAttribute('aria-label', 'Axel the Loan Lion chat assistant');
        panel.innerHTML = '' +
            '<div class="axel-chat-header">' +
                '<div class="axel-chat-avatar-wrap">' +
                    '<img class="axel-chat-avatar" src="/axel-loan-lion.png" alt="Axel the Loan Lion">' +
                    '<span class="axel-chat-avatar-fallback" aria-hidden="true">🦁</span>' +
                '</div>' +
                '<div class="axel-chat-title-wrap">' +
                    '<h3>Axel the Loan Lion</h3>' +
                    '<p>AI Lending Assistant</p>' +
                '</div>' +
                '<button class="axel-chat-close" type="button" aria-label="Close chat">✕</button>' +
            '</div>' +
            '<div class="axel-chat-messages" id="axelChatMessages"></div>' +
            '<div class="axel-chat-quick" id="axelChatQuick">' +
                '<button type="button" data-q="What financing options do you offer?">Financing options</button>' +
                '<button type="button" data-q="How fast can I get funded?">Funding timeline</button>' +
                '<button type="button" data-q="What credit score do lenders prefer?">Credit requirements</button>' +
            '</div>' +
            '<form class="axel-chat-input-row" id="axelChatForm">' +
                '<input id="axelChatInput" type="text" placeholder="Ask Axel about funding..." autocomplete="off" />' +
                '<button type="submit">Send</button>' +
            '</form>';

        document.body.appendChild(launcher);
        document.body.appendChild(panel);

        const avatar = panel.querySelector('.axel-chat-avatar');
        const avatarFallback = panel.querySelector('.axel-chat-avatar-fallback');
        if (avatar) {
            avatar.addEventListener('error', function onAvatarError() {
                avatar.removeEventListener('error', onAvatarError);
                avatar.style.display = 'none';
                if (avatarFallback) avatarFallback.style.display = 'inline-flex';
            });
        }

        const messages = panel.querySelector('#axelChatMessages');
        const form = panel.querySelector('#axelChatForm');
        const input = panel.querySelector('#axelChatInput');
        const close = panel.querySelector('.axel-chat-close');
        const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const isMobileViewport = window.matchMedia && window.matchMedia('(max-width: 768px)').matches;
        const chatHistory = [];

        function addMessage(role, text) {
            if (!messages) return;
            const msg = document.createElement('div');
            msg.className = 'axel-chat-message ' + role;
            msg.textContent = text;
            messages.appendChild(msg);
            messages.scrollTop = messages.scrollHeight;
        }

        function makeReply(text, actions) {
            return {
                text: text,
                actions: Array.isArray(actions) ? actions : []
            };
        }

        function addBotMessage(payload) {
            if (!messages) return;
            const reply = (typeof payload === 'string') ? makeReply(payload) : payload;
            const msg = document.createElement('div');
            msg.className = 'axel-chat-message bot';
            msg.textContent = reply && reply.text ? reply.text : '';

            if (reply && Array.isArray(reply.actions) && reply.actions.length) {
                const actions = document.createElement('div');
                actions.className = 'axel-chat-actions';
                reply.actions.forEach(function(action) {
                    if (!action || !action.href || !action.label) return;
                    const link = document.createElement('a');
                    link.className = 'axel-chat-action';
                    link.href = action.href;
                    link.textContent = action.label;
                    actions.appendChild(link);
                });
                if (actions.children.length) {
                    msg.appendChild(actions);
                }
            }

            messages.appendChild(msg);
            messages.scrollTop = messages.scrollHeight;
        }

        function pushHistory(role, text) {
            chatHistory.push({ role: role, text: text, time: Date.now() });
            if (chatHistory.length > 12) {
                chatHistory.splice(0, chatHistory.length - 12);
            }
        }

        function scoreIntent(query, keywords) {
            let score = 0;
            keywords.forEach(function(word) {
                if (query.indexOf(word) !== -1) score += 1;
            });
            return score;
        }

        function getIntent(query) {
            const intents = [
                { name: 'greeting', words: ['hello', 'hi ', 'hey', 'good morning', 'good afternoon', 'good evening'] },
                { name: 'credit', words: ['credit', 'fico', 'score', 'bankrupt', 'bankruptcy', 'collections'] },
                { name: 'timeline', words: ['how fast', 'timeline', 'fund', 'funding', 'approval', 'close', 'days', 'weeks'] },
                { name: 'sba', words: ['sba', '7a', '504'] },
                { name: 'equipment', words: ['equipment', 'machinery', 'truck', 'vehicle', 'lease'] },
                { name: 'loc', words: ['line of credit', 'loc', 'revolving', 'draw'] },
                { name: 'working_capital', words: ['working capital', 'payroll', 'inventory', 'cash flow'] },
                { name: 'term_loan', words: ['term loan', 'lump sum', 'fixed payment'] },
                { name: 'cre', words: ['commercial real estate', 'cre', 'property', 'owner occupied', 'refinance', 'acquisition'] },
                { name: 'referral', words: ['referral', 'commission', 'agreement', 'partner program'] },
                { name: 'contact', words: ['contact', 'call', 'human', 'agent', 'speak', 'talk to someone'] }
            ];

            let best = { name: 'general', score: 0 };
            intents.forEach(function(intent) {
                const s = scoreIntent(query, intent.words);
                if (s > best.score) best = { name: intent.name, score: s };
            });
            return best.score > 0 ? best.name : 'general';
        }

        function getContextHint() {
            if (!chatHistory.length) return '';
            const recentUser = chatHistory.slice().reverse().find(function(item) { return item.role === 'user'; });
            if (!recentUser) return '';
            return recentUser.text.toLowerCase();
        }

        function getReply(raw) {
            const q = String(raw || '').trim().toLowerCase();
            const hint = getContextHint();
            const intent = getIntent(q);
            if (!q) {
                return makeReply(
                    'Tell me what you are trying to fund, how much you need, and when you need it. I will suggest the best path.',
                    [{ label: 'Start Application', href: '/match.html' }]
                );
            }

            if (intent === 'greeting') {
                return makeReply(
                    'Great to meet you. I am Axel the Loan Lion. If you share your funding amount, use of funds, and timing, I can point you to the best program right away.',
                    [{ label: 'Find My Match', href: '/match.html' }]
                );
            }

            if (intent === 'credit') {
                return makeReply(
                    'Credit score matters, but lenders review the full profile: revenue consistency, time in business, recent bank activity, and debt coverage. Stronger credit usually improves pricing and approval odds. If you share your approximate score range and monthly revenue, I can suggest the best-fit options.',
                    [{ label: 'Talk to Team', href: '/contact.html' }, { label: 'Apply Now', href: '/match.html' }]
                );
            }

            if (intent === 'timeline') {
                return makeReply(
                    'Funding speed depends on product and documentation quality. Faster products can move quickly when statements and purpose are clear, while SBA and larger structured deals usually take longer. If you tell me your target funding date, I can recommend a speed-first option.',
                    [{ label: 'Get Started', href: '/match.html' }]
                );
            }

            if (intent === 'sba') {
                return makeReply(
                    'SBA financing is best for longer terms and lower monthly payment pressure when your profile is strong. Common use cases include working capital, expansion, equipment, and owner-occupied real estate.',
                    [{ label: 'View SBA Loans', href: '/sba-loans.html' }, { label: 'Apply for SBA Match', href: '/match.html' }]
                );
            }

            if (intent === 'equipment') {
                return makeReply(
                    'Equipment financing can preserve cash by spreading costs over time while matching payments to useful life. It is commonly used for vehicles, heavy machinery, and specialized equipment.',
                    [{ label: 'View Equipment Financing', href: '/equipment-financing.html' }]
                );
            }

            if (intent === 'loc') {
                return makeReply(
                    'A business line of credit is flexible revolving capital for short-term needs like inventory, payroll timing, and receivables gaps. You draw what you need and reuse availability as you repay.',
                    [{ label: 'View Line of Credit', href: '/business-line-of-credit.html' }]
                );
            }

            if (intent === 'working_capital') {
                return makeReply(
                    'Working capital loans are designed for day-to-day operations, seasonal gaps, and growth moments where cash timing matters. They are often simpler and faster than long-form loans.',
                    [{ label: 'View Working Capital', href: '/working-capital-loans.html' }]
                );
            }

            if (intent === 'term_loan') {
                return makeReply(
                    'Business term loans are useful when you need a lump sum with predictable repayment for expansion, refinance, or strategic investments. They are typically structured around cash flow strength.',
                    [{ label: 'View Term Loans', href: '/business-term-loans.html' }]
                );
            }

            if (intent === 'cre') {
                return makeReply(
                    'Commercial real estate financing is commonly used for acquisition, refinance, and owner-occupied properties. Structure depends on occupancy, cash flow, and property type.',
                    [{ label: 'View CRE Loans', href: '/commercial-real-estate-loans.html' }]
                );
            }

            if (intent === 'referral') {
                return makeReply(
                    'You can review the full referral terms and download the agreement on the referral page.',
                    [{ label: 'Open Referral Agreement', href: '/referral.html' }]
                );
            }

            if (intent === 'contact') {
                return makeReply(
                    'I can connect you to the team directly. If you want, I can also help you prepare the exact details to send so underwriting can review faster.',
                    [{ label: 'Contact Team', href: '/contact.html' }]
                );
            }

            if (hint.indexOf('credit') !== -1 && q.indexOf('what about') !== -1) {
                return makeReply(
                    'If credit is your main concern, we can often still identify viable structures by balancing score with cash flow and purpose. Share your score range, revenue trend, and funding need, and I will map next-best options.',
                    [{ label: 'See Options', href: '/services.html' }]
                );
            }

            return makeReply(
                'I can give a precise recommendation if you share 3 things: funding amount, use of funds, and how fast you need it.',
                [{ label: 'Start Application', href: '/match.html' }, { label: 'View Services', href: '/services.html' }]
            );
        }

        function setThinking(isThinking) {
            if (!messages) return null;
            if (!isThinking) {
                const existing = messages.querySelector('.axel-chat-message.bot.thinking');
                if (existing) existing.remove();
                return null;
            }
            const thinking = document.createElement('div');
            thinking.className = 'axel-chat-message bot thinking';
            thinking.textContent = 'Axel is thinking...';
            messages.appendChild(thinking);
            messages.scrollTop = messages.scrollHeight;
            return thinking;
        }

        function handleSend(text) {
            const prompt = (text || '').trim();
            if (!prompt) return;
            addMessage('user', prompt);
            pushHistory('user', prompt);
            const thinkingNode = setThinking(true);
            window.setTimeout(function() {
                if (thinkingNode) thinkingNode.remove();
                const reply = getReply(prompt);
                addBotMessage(reply);
                pushHistory('bot', reply && reply.text ? reply.text : String(reply || ''));
            }, 320);
        }

        function openChat(shouldFocusInput) {
            panel.classList.add('open');
            launcher.classList.add('open');
            if (messages && !messages.dataset.seeded) {
                messages.dataset.seeded = '1';
                addBotMessage(makeReply(
                    'Hi, I am Axel the Loan Lion. Ask me about business financing and I will point you in the right direction.',
                    [{ label: 'Get Matched', href: '/match.html' }]
                ));
            }
            if (shouldFocusInput && input && !isMobileViewport) input.focus();
        }

        launcher.addEventListener('click', function() {
            const willOpen = !panel.classList.contains('open');
            if (willOpen) {
                openChat(true);
            } else {
                panel.classList.remove('open');
                launcher.classList.remove('open');
            }
        });

        if (close) {
            close.addEventListener('click', function() {
                panel.classList.remove('open');
                launcher.classList.remove('open');
            });
        }

        if (form && input) {
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                handleSend(input.value);
                input.value = '';
            });
        }

        panel.querySelectorAll('.axel-chat-quick button').forEach(function(btn) {
            btn.addEventListener('click', function() {
                const q = btn.getAttribute('data-q') || '';
                handleSend(q);
            });
        });

        // Auto-open Axel when each tab/page loads.
        let shouldAutoOpen = true;
        try {
            shouldAutoOpen = localStorage.getItem(autoOpenKey) !== '1';
        } catch (error) {
            shouldAutoOpen = true;
        }

        if (shouldAutoOpen && !isMobileViewport) {
            window.setTimeout(function() {
                openChat(false);
                try {
                    localStorage.setItem(autoOpenKey, '1');
                } catch (error) {
                    // Ignore storage restrictions and keep behavior non-blocking.
                }
                if (!prefersReducedMotion) {
                    panel.classList.add('axel-chat-pop');
                    window.setTimeout(function() {
                        panel.classList.remove('axel-chat-pop');
                    }, 900);
                }
            }, 700);
        }
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

    function enhanceIndustryPageLayout() {
        const container = document.querySelector('.form-container.industry-page-content');
        if (!container || container.dataset.industryEnhanced === '1') return;

        const introEl = container.querySelector('.results-intro');
        const introHtml = introEl ? (introEl.innerHTML || introEl.textContent || '').trim() : '';
        if (introEl) introEl.remove();
        const sections = container.querySelectorAll('.about-section');
        if (!sections.length) return;

        container.dataset.industryEnhanced = '1';

        const tocList = document.createElement('ul');
        tocList.className = 'blog-post-toc-list';
        let sectionCounter = 0;

        sections.forEach(function(section) {
            const h2 = section.querySelector(':scope > h2');
            if (!h2) return;

            sectionCounter += 1;
            const base = slugifyHeading(h2.textContent) || ('section-' + sectionCounter);
            const id = 'section-' + sectionCounter + '-' + base;
            h2.id = id;

            const tocItem = document.createElement('li');
            const tocLink = document.createElement('a');
            tocLink.href = '#' + id;
            tocLink.textContent = h2.textContent.trim();
            tocItem.appendChild(tocLink);
            tocList.appendChild(tocItem);
        });

        const railRight = document.createElement('aside');
        railRight.className = 'industry-page-rail';

        if (introHtml) {
            const summaryCard = document.createElement('div');
            summaryCard.className = 'blog-rail-card blog-rail-meta industry-rail-summary';
            summaryCard.innerHTML = '<h3>Summary</h3><div class="blog-rail-description"><p>' + introHtml + '</p></div>';
            railRight.appendChild(summaryCard);
        }

        if (tocList.children.length) {
            const tocCard = document.createElement('div');
            tocCard.className = 'blog-rail-card blog-rail-toc';
            const title = document.createElement('h3');
            title.textContent = 'On This Page';
            tocCard.appendChild(title);
            tocCard.appendChild(tocList);
            railRight.appendChild(tocCard);
        }

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

        const shell = document.createElement('div');
        shell.className = 'industry-page-shell';
        const main = document.createElement('div');
        main.className = 'industry-page-main';
        Array.from(container.children).forEach(function(child) {
            if (child.classList && child.classList.contains('results-intro')) return;
            main.appendChild(child);
        });
        shell.appendChild(main);
        shell.appendChild(railRight);
        container.appendChild(shell);
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
        const introNodes = allChildren.slice(0, contentStartIdx);
        const articleNodes = allChildren.slice(contentStartIdx);

        var bylineText = '';
        var leadHtml = '';
        var backLinkHtml = '';
        var filteredIntroNodes = [];
        introNodes.forEach(function(node) {
            if (node.classList && node.classList.contains('blog-byline')) {
                bylineText = (node.textContent || '').trim();
                return;
            }
            if (node.classList && node.classList.contains('blog-lead')) {
                leadHtml = (node.innerHTML || node.textContent || '').trim();
                return;
            }
            if (node.classList && node.classList.contains('blog-back')) {
                backLinkHtml = (node.innerHTML || '').trim();
                return;
            }
            /* Skip any node that contains blog intro—avoids re-appending wrapped intro on mobile */
            if (node.querySelector && node.querySelector('.blog-back, .blog-byline, .blog-lead')) {
                return;
            }
            filteredIntroNodes.push(node);
        });
        var introToUse = filteredIntroNodes;

        const shell = document.createElement('div');
        shell.className = 'blog-post-shell';

        const main = document.createElement('article');
        main.className = 'blog-post-main';

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
        const calculatedMinutes = Math.max(3, Math.round(totalWords / 200));
        var readMinutes = calculatedMinutes;
        var minReadMatch = bylineText.match(/(\d+)\s*min\s*read/i);
        if (minReadMatch) {
            readMinutes = Math.max(1, parseInt(minReadMatch[1], 10));
        }

        var lastUpdatedHtml = '';
        if (bylineText) {
            if (/last\s*updated\s*:/i.test(bylineText)) {
                var match = bylineText.match(/last\s*updated\s*:\s*([^·\-]+)/i);
                lastUpdatedHtml = '<p class="blog-rail-meta-item"><span class="blog-rail-label">Last updated:</span> <strong>' + (match ? match[1].trim() : bylineText) + '</strong></p>';
            } else {
                lastUpdatedHtml = '<p class="blog-rail-meta-item"><span class="blog-rail-label">Updated:</span> <strong>' + String(bylineText).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;') + '</strong></p>';
            }
        }
        var readTimeHtml = '<p class="blog-rail-meta-item"><span class="blog-rail-label">Read time:</span> <strong>' + readMinutes + ' min</strong></p>';
        var descriptionHtml = '';
        if (leadHtml) {
            descriptionHtml = '<div class="blog-rail-description"><span class="blog-rail-label">Summary</span><p>' + leadHtml + '</p></div>';
        }

        var railLeft = document.createElement('div');
        railLeft.className = 'blog-post-rail-left';
        var backLinkBlock = backLinkHtml ? '<p class="blog-rail-back">' + backLinkHtml + '</p>' : '';
        railLeft.innerHTML = '' +
            '<div class="blog-rail-card blog-rail-meta">' +
                backLinkBlock +
                '<h3>Article Guide</h3>' +
                lastUpdatedHtml +
                readTimeHtml +
                descriptionHtml +
            '</div>';

        var railRight = document.createElement('aside');
        railRight.className = 'blog-post-rail-right';
        if (tocList.children.length) {
            const tocCard = document.createElement('div');
            tocCard.className = 'blog-rail-card blog-rail-toc';
            const title = document.createElement('h3');
            title.textContent = 'On This Page';
            tocCard.appendChild(title);
            tocCard.appendChild(tocList);
            railRight.appendChild(tocCard);
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

        shell.appendChild(railLeft);
        shell.appendChild(main);
        if (railRight.children.length) {
            shell.appendChild(railRight);
        } else {
            shell.classList.add('blog-post-shell--no-toc');
        }

        container.innerHTML = '';
        introToUse.forEach(function(node) { container.appendChild(node); });
        container.appendChild(shell);
    }

    function hashString(input) {
        let hash = 0;
        const value = String(input || '');
        for (let i = 0; i < value.length; i += 1) {
            hash = ((hash << 5) - hash) + value.charCodeAt(i);
            hash |= 0;
        }
        return Math.abs(hash);
    }

    function getVisualIdentity(url) {
        const value = String(url || '');
        const match = value.match(/photo-[^?&/]+/i);
        return match ? match[0].toLowerCase() : value.toLowerCase();
    }

    function getRecentServiceVisuals() {
        const key = 'axiantRecentServiceVisualsV1';
        try {
            const raw = localStorage.getItem(key);
            if (!raw) return new Set();
            const list = JSON.parse(raw);
            if (!Array.isArray(list)) return new Set();
            return new Set(list.map(function(item) { return String(item || '').toLowerCase(); }).filter(Boolean));
        } catch (error) {
            return new Set();
        }
    }

    function saveRecentServiceVisuals(recentVisuals) {
        const key = 'axiantRecentServiceVisualsV1';
        try {
            const list = Array.from(recentVisuals).filter(Boolean);
            // Keep a larger rolling history to avoid repeats across many visits/pages.
            const trimmed = list.slice(-500);
            localStorage.setItem(key, JSON.stringify(trimmed));
        } catch (error) {
            // Ignore storage limitations/private browsing constraints.
        }
    }

    function pickVisualUrl(list, seed, usedVisuals, recentVisuals) {
        if (!Array.isArray(list) || !list.length) return '';
        const base = hashString(seed);
        // Pass 1: avoid page duplicates and recent service-page history.
        for (let i = 0; i < list.length; i += 1) {
            const candidate = list[(base + i) % list.length];
            const identity = getVisualIdentity(candidate);
            if (!usedVisuals.has(identity) && (!recentVisuals || !recentVisuals.has(identity))) {
                usedVisuals.add(identity);
                if (recentVisuals) recentVisuals.add(identity);
                return candidate;
            }
        }
        // Pass 2: always prioritize unique-on-page rendering (ignore recent history).
        for (let i = 0; i < list.length; i += 1) {
            const candidate = list[(base + i) % list.length];
            const identity = getVisualIdentity(candidate);
            if (!usedVisuals.has(identity)) {
                usedVisuals.add(identity);
                if (recentVisuals) recentVisuals.add(identity);
                return candidate;
            }
        }
        // Strict no-repeat mode for current page once pool is exhausted.
        return '';
    }

    function pickVisualUrlOrdered(list, cursorKey, cursors, usedVisuals, recentVisuals) {
        if (!Array.isArray(list) || !list.length) return '';
        const start = Math.max(0, Number(cursors[cursorKey] || 0)) % list.length;
        // Pass 1: avoid page duplicates and recent service-page history.
        for (let i = 0; i < list.length; i += 1) {
            const idx = (start + i) % list.length;
            const candidate = list[idx];
            const identity = getVisualIdentity(candidate);
            if (!usedVisuals.has(identity) && (!recentVisuals || !recentVisuals.has(identity))) {
                usedVisuals.add(identity);
                if (recentVisuals) recentVisuals.add(identity);
                cursors[cursorKey] = (idx + 1) % list.length;
                return candidate;
            }
        }
        // Pass 2: always prioritize unique-on-page rendering (ignore recent history).
        for (let i = 0; i < list.length; i += 1) {
            const idx = (start + i) % list.length;
            const candidate = list[idx];
            const identity = getVisualIdentity(candidate);
            if (!usedVisuals.has(identity)) {
                usedVisuals.add(identity);
                if (recentVisuals) recentVisuals.add(identity);
                cursors[cursorKey] = (idx + 1) % list.length;
                return candidate;
            }
        }
        return '';
    }

    function getPageArtDirection(page) {
        const plans = {
            'sba-loans.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 2, variant: 'side', pool: 'inline' }, { index: 4, variant: 'side', pool: 'card' }],
                sectionCaption: 'Structured SBA funding'
            },
            'equipment-financing.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 1, variant: 'side', pool: 'inline' }, { index: 3, variant: 'side', pool: 'card' }],
                sectionCaption: 'Equipment-driven growth'
            },
            'business-line-of-credit.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'inline' }, { index: 2, variant: 'side', pool: 'card' }, { index: 4, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Flexible credit access'
            },
            'working-capital-loans.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'inline' }, { index: 1, variant: 'side', pool: 'card' }, { index: 3, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Operational momentum capital'
            },
            'working-capital.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'inline' }, { index: 1, variant: 'side', pool: 'card' }, { index: 2, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Daily operating capital'
            },
            'business-term-loans.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 2, variant: 'side', pool: 'card' }, { index: 4, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Planned long-term growth'
            },
            'commercial-real-estate-loans.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 1, variant: 'side', pool: 'card' }, { index: 3, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Commercial property ownership'
            },
            'commercial-bridge-loans.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 1, variant: 'side', pool: 'inline' }, { index: 2, variant: 'side', pool: 'card' }],
                sectionCaption: 'Bridge transition timing'
            },
            'revenue-based-financing.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'inline' }, { index: 1, variant: 'side', pool: 'card' }, { index: 3, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Sales-driven capital'
            },
            'securities-based-lending.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 1, variant: 'side', pool: 'inline' }, { index: 2, variant: 'side', pool: 'card' }],
                sectionCaption: 'Sophisticated asset leverage'
            },
            'fix-and-flip.html': {
                textSectionPlan: [{ index: 0, variant: 'compact', pool: 'banner' }, { index: 1, variant: 'side', pool: 'card' }, { index: 3, variant: 'side', pool: 'inline' }],
                sectionCaption: 'Renovation and turnaround'
            }
        };
        return plans[page] || null;
    }

    function getGuidedCardImagePool(title) {
        const value = String(title || '').toLowerCase();
        if (value.indexOf('equipment selection') !== -1) {
            return [
                'assets/ai-equipment-1.png'
            ];
        }
        if (value.indexOf('application review') !== -1) {
            return [
                'assets/ai-equipment-3.png'
            ];
        }
        if (value.indexOf('receive approval') !== -1) {
            return [
                'assets/ai-equipment-4.png'
            ];
        }
        if (value.indexOf('funding & vendor payment') !== -1 || value.indexOf('funding and vendor payment') !== -1) {
            return [
                'assets/ai-equipment-5.png'
            ];
        }
        if (value.indexOf('submit your information') !== -1) {
            return [
                'assets/ai-howitworks-1.png'
            ];
        }
        if (value.indexOf('match you internally') !== -1) {
            return [
                'assets/ai-howitworks-2.png'
            ];
        }
        if (value.indexOf('we call you') !== -1) {
            return [
                'assets/ai-howitworks-3.png'
            ];
        }
        if (value.indexOf('banks contact you') !== -1) {
            return [
                'assets/ai-howitworks-4.png'
            ];
        }
        if (value.indexOf('application & documentation') !== -1 || value.indexOf('application and documentation') !== -1) {
            return [
                'assets/ai-sba-3.png'
            ];
        }
        if (value.indexOf('underwriting & sba review') !== -1 || value.indexOf('underwriting and sba review') !== -1) {
            return [
                'assets/ai-sba-4.png'
            ];
        }
        if (value.indexOf('approval & closing') !== -1 || value.indexOf('approval and closing') !== -1) {
            return [
                'assets/ai-sba-5.png'
            ];
        }
        if (value.indexOf('funding') !== -1) {
            return [
                'assets/ai-sba-6.png'
            ];
        }
        if (value.indexOf('save time') !== -1) {
            return [
                'assets/ai-whyaxiant-1.png'
            ];
        }
        if (value.indexOf('higher approval rates') !== -1) {
            return [
                'assets/ai-whyaxiant-2.png'
            ];
        }
        if (value.indexOf('secure and private') !== -1) {
            return [
                'assets/ai-whyaxiant-3.png'
            ];
        }
        if (value.indexOf('premium relationships') !== -1) {
            return [
                'assets/ai-whyaxiant-4.png'
            ];
        }
        if (value.indexOf('personal service') !== -1) {
            return [
                'assets/ai-whyaxiant-5.png'
            ];
        }
        if (value.indexOf('no cost to you') !== -1) {
            return [
                'assets/ai-whyaxiant-6.png'
            ];
        }
        return null;
    }

    function resolveVisualAsset(url) {
        const value = String(url || '');
        if (!value) return '';
        if (/^(https?:)?\/\//i.test(value) || value.startsWith('data:')) return value;
        return '/' + value.replace(/^\/+/, '');
    }

    function resolveVisualSet(rawSet) {
        const visual = rawSet || {};
        return {
            banner: (visual.banner || []).map(resolveVisualAsset),
            card: (visual.card || []).map(resolveVisualAsset),
            inline: (visual.inline || []).map(resolveVisualAsset),
            caption: visual.caption || ''
        };
    }

    function buildVisualRange(prefix, count) {
        const list = [];
        for (let i = 1; i <= count; i += 1) {
            list.push('assets/' + prefix + '-' + i + '.png');
        }
        return list;
    }

    function getUniversalVisualPool() {
        const raw = []
            .concat(buildVisualRange('ai-equipment', 5))
            .concat(buildVisualRange('ai-realestate', 5))
            .concat(buildVisualRange('ai-sba', 6))
            .concat(buildVisualRange('ai-bridge', 5))
            .concat(buildVisualRange('ai-fixflip', 5))
            .concat(buildVisualRange('ai-linecredit', 5))
            .concat(buildVisualRange('ai-workingcapital', 5))
            .concat(buildVisualRange('ai-termloans', 5))
            .concat(buildVisualRange('ai-revenue', 5))
            .concat(buildVisualRange('ai-securities', 4))
            .concat(buildVisualRange('ai-growth', 3))
            .concat(buildVisualRange('ai-blog', 5))
            .concat(buildVisualRange('ai-howitworks', 4))
            .concat(buildVisualRange('ai-whyaxiant', 6));
        return raw.map(resolveVisualAsset);
    }

    function getTopicVisualSet() {
        const path = (window.location.pathname || '').toLowerCase();
        const page = path.split('/').pop() || 'index.html';

        const sets = {
            equipment: {
                banner: [
                    'assets/ai-equipment-1.png',
                    'assets/ai-equipment-2.png',
                    'assets/ai-equipment-3.png',
                    'assets/ai-equipment-4.png',
                    'assets/ai-equipment-5.png'
                ],
                card: [
                    'assets/ai-equipment-1.png',
                    'assets/ai-equipment-2.png',
                    'assets/ai-equipment-3.png',
                    'assets/ai-equipment-4.png',
                    'assets/ai-equipment-5.png'
                ],
                inline: [
                    'assets/ai-equipment-1.png',
                    'assets/ai-equipment-2.png',
                    'assets/ai-equipment-3.png',
                    'assets/ai-equipment-4.png',
                    'assets/ai-equipment-5.png'
                ],
                caption: 'Equipment financing insights'
            },
            realEstate: {
                banner: [
                    'assets/ai-realestate-1.png',
                    'assets/ai-realestate-2.png',
                    'assets/ai-realestate-3.png',
                    'assets/ai-realestate-4.png',
                    'assets/ai-realestate-5.png'
                ],
                card: [
                    'assets/ai-realestate-1.png',
                    'assets/ai-realestate-2.png',
                    'assets/ai-realestate-3.png',
                    'assets/ai-realestate-4.png',
                    'assets/ai-realestate-5.png'
                ],
                inline: [
                    'assets/ai-realestate-1.png',
                    'assets/ai-realestate-2.png',
                    'assets/ai-realestate-3.png',
                    'assets/ai-realestate-4.png',
                    'assets/ai-realestate-5.png'
                ],
                caption: 'Commercial real estate funding'
            },
            sba: {
                banner: [
                    'assets/ai-sba-1.png',
                    'assets/ai-sba-2.png',
                    'assets/ai-sba-3.png',
                    'assets/ai-sba-4.png',
                    'assets/ai-sba-5.png',
                    'assets/ai-sba-6.png'
                ],
                card: [
                    'assets/ai-sba-1.png',
                    'assets/ai-sba-2.png',
                    'assets/ai-sba-3.png',
                    'assets/ai-sba-4.png',
                    'assets/ai-sba-5.png',
                    'assets/ai-sba-6.png'
                ],
                inline: [
                    'assets/ai-sba-1.png',
                    'assets/ai-sba-2.png',
                    'assets/ai-sba-3.png',
                    'assets/ai-sba-4.png',
                    'assets/ai-sba-5.png',
                    'assets/ai-sba-6.png'
                ],
                caption: 'SBA loan strategies'
            },
            bridge: {
                banner: [
                    'assets/ai-bridge-1.png',
                    'assets/ai-bridge-2.png',
                    'assets/ai-bridge-3.png',
                    'assets/ai-bridge-4.png',
                    'assets/ai-bridge-5.png'
                ],
                card: [
                    'assets/ai-bridge-1.png',
                    'assets/ai-bridge-2.png',
                    'assets/ai-bridge-3.png',
                    'assets/ai-bridge-4.png',
                    'assets/ai-bridge-5.png'
                ],
                inline: [
                    'assets/ai-bridge-1.png',
                    'assets/ai-bridge-2.png',
                    'assets/ai-bridge-3.png',
                    'assets/ai-bridge-4.png',
                    'assets/ai-bridge-5.png'
                ],
                caption: 'Bridge and transition financing'
            },
            fixFlip: {
                banner: [
                    'assets/ai-fixflip-1.png',
                    'assets/ai-fixflip-2.png',
                    'assets/ai-fixflip-3.png',
                    'assets/ai-fixflip-4.png',
                    'assets/ai-fixflip-5.png'
                ],
                card: [
                    'assets/ai-fixflip-1.png',
                    'assets/ai-fixflip-2.png',
                    'assets/ai-fixflip-3.png',
                    'assets/ai-fixflip-4.png',
                    'assets/ai-fixflip-5.png'
                ],
                inline: [
                    'assets/ai-fixflip-1.png',
                    'assets/ai-fixflip-2.png',
                    'assets/ai-fixflip-3.png',
                    'assets/ai-fixflip-4.png',
                    'assets/ai-fixflip-5.png'
                ],
                caption: 'Fix and flip renovation financing'
            },
            growth: {
                banner: [
                    'assets/ai-growth-1.png',
                    'assets/ai-growth-2.png',
                    'assets/ai-growth-3.png',
                    'assets/ai-termloans-3.png',
                    'assets/ai-workingcapital-5.png'
                ],
                card: [
                    'assets/ai-growth-1.png',
                    'assets/ai-growth-2.png',
                    'assets/ai-growth-3.png',
                    'assets/ai-termloans-4.png',
                    'assets/ai-workingcapital-3.png',
                    'assets/ai-linecredit-5.png'
                ],
                inline: [
                    'assets/ai-growth-1.png',
                    'assets/ai-growth-2.png',
                    'assets/ai-growth-3.png',
                    'assets/ai-termloans-5.png',
                    'assets/ai-workingcapital-4.png',
                    'assets/ai-linecredit-3.png',
                    'assets/ai-revenue-3.png'
                ],
                caption: 'Business growth and capital planning'
            },
            lineCredit: {
                banner: [
                    'assets/ai-linecredit-1.png',
                    'assets/ai-linecredit-2.png',
                    'assets/ai-linecredit-3.png',
                    'assets/ai-linecredit-4.png',
                    'assets/ai-linecredit-5.png'
                ],
                card: [
                    'assets/ai-linecredit-1.png',
                    'assets/ai-linecredit-2.png',
                    'assets/ai-linecredit-3.png',
                    'assets/ai-linecredit-4.png',
                    'assets/ai-linecredit-5.png'
                ],
                inline: [
                    'assets/ai-linecredit-1.png',
                    'assets/ai-linecredit-2.png',
                    'assets/ai-linecredit-3.png',
                    'assets/ai-linecredit-4.png',
                    'assets/ai-linecredit-5.png'
                ],
                caption: 'Business line of credit flexibility'
            },
            workingCapital: {
                banner: [
                    'assets/ai-workingcapital-1.png',
                    'assets/ai-workingcapital-2.png',
                    'assets/ai-workingcapital-3.png',
                    'assets/ai-workingcapital-4.png',
                    'assets/ai-workingcapital-5.png'
                ],
                card: [
                    'assets/ai-workingcapital-1.png',
                    'assets/ai-workingcapital-2.png',
                    'assets/ai-workingcapital-3.png',
                    'assets/ai-workingcapital-4.png',
                    'assets/ai-workingcapital-5.png'
                ],
                inline: [
                    'assets/ai-workingcapital-1.png',
                    'assets/ai-workingcapital-2.png',
                    'assets/ai-workingcapital-3.png',
                    'assets/ai-workingcapital-4.png',
                    'assets/ai-workingcapital-5.png'
                ],
                caption: 'Working capital for daily operations'
            },
            termLoans: {
                banner: [
                    'assets/ai-termloans-1.png',
                    'assets/ai-termloans-2.png',
                    'assets/ai-termloans-3.png',
                    'assets/ai-termloans-4.png',
                    'assets/ai-termloans-5.png'
                ],
                card: [
                    'assets/ai-termloans-1.png',
                    'assets/ai-termloans-2.png',
                    'assets/ai-termloans-3.png',
                    'assets/ai-termloans-4.png',
                    'assets/ai-termloans-5.png'
                ],
                inline: [
                    'assets/ai-termloans-1.png',
                    'assets/ai-termloans-2.png',
                    'assets/ai-termloans-3.png',
                    'assets/ai-termloans-4.png',
                    'assets/ai-termloans-5.png'
                ],
                caption: 'Structured business term loan growth'
            },
            revenueBased: {
                banner: [
                    'assets/ai-revenue-1.png',
                    'assets/ai-revenue-2.png',
                    'assets/ai-revenue-3.png',
                    'assets/ai-revenue-4.png',
                    'assets/ai-revenue-5.png'
                ],
                card: [
                    'assets/ai-revenue-1.png',
                    'assets/ai-revenue-2.png',
                    'assets/ai-revenue-3.png',
                    'assets/ai-revenue-4.png',
                    'assets/ai-revenue-5.png'
                ],
                inline: [
                    'assets/ai-revenue-1.png',
                    'assets/ai-revenue-2.png',
                    'assets/ai-revenue-3.png',
                    'assets/ai-revenue-4.png',
                    'assets/ai-revenue-5.png'
                ],
                caption: 'Revenue-driven funding momentum'
            },
            securities: {
                banner: [
                    'assets/ai-securities-1.png',
                    'assets/ai-securities-2.png',
                    'assets/ai-securities-3.png',
                    'assets/ai-securities-4.png'
                ],
                card: [
                    'assets/ai-securities-1.png',
                    'assets/ai-securities-2.png',
                    'assets/ai-securities-3.png',
                    'assets/ai-securities-4.png'
                ],
                inline: [
                    'assets/ai-securities-1.png',
                    'assets/ai-securities-2.png',
                    'assets/ai-securities-3.png',
                    'assets/ai-securities-4.png'
                ],
                caption: 'Sophisticated asset-backed lending'
            },
            blog: {
                banner: [
                    'assets/ai-blog-1.png',
                    'assets/ai-blog-2.png',
                    'assets/ai-blog-3.png',
                    'assets/ai-blog-4.png',
                    'assets/ai-blog-5.png'
                ],
                card: [
                    'assets/ai-blog-1.png',
                    'assets/ai-blog-2.png',
                    'assets/ai-blog-3.png',
                    'assets/ai-blog-4.png',
                    'assets/ai-blog-5.png'
                ],
                inline: [
                    'assets/ai-blog-1.png',
                    'assets/ai-blog-2.png',
                    'assets/ai-blog-3.png',
                    'assets/ai-blog-4.png',
                    'assets/ai-blog-5.png'
                ],
                caption: 'Funding guides and industry insights'
            }
        };

        const curatedPageSet = {
            // Core site pages
            'index.html': 'growth',
            'services.html': 'growth',
            'contact.html': 'growth',
            'calculator.html': 'growth',
            'faq.html': 'growth',
            'match.html': 'growth',
            'vendors.html': 'growth',
            'glossary.html': 'growth',
            'referral.html': 'growth',
            'rightmfgsystems.html': 'growth',

            // Equipment financing pages
            'equipment-financing.html': 'equipment',
            'equipment-financing-contractors.html': 'equipment',
            'bad-credit-equipment-financing.html': 'equipment',
            'bucket-truck-financing.html': 'equipment',
            'cnc-machine-financing.html': 'equipment',
            'construction-equipment-financing.html': 'equipment',
            'dozer-financing.html': 'equipment',
            'dump-truck-financing.html': 'equipment',
            'excavator-financing.html': 'equipment',
            'farm-agriculture-equipment-financing.html': 'equipment',
            'food-service-equipment-loans.html': 'equipment',
            'heavy-equipment-loans.html': 'equipment',
            'manufacturing-equipment-financing.html': 'equipment',
            'medical-equipment-financing.html': 'equipment',
            'no-doc-equipment-financing.html': 'equipment',
            'office-equipment-financing.html': 'equipment',
            'one-year-in-business-equipment-loan.html': 'equipment',
            'same-day-equipment-approval.html': 'equipment',
            'skid-steer-financing.html': 'equipment',
            'startup-equipment-financing.html': 'equipment',
            'trailer-financing.html': 'equipment',
            'truck-trailer-financing.html': 'equipment',
            'used-equipment-loans.html': 'equipment',
            'wood-chipper-grinder-financing.html': 'equipment',

            // CRE and bridge lending pages
            'commercial-real-estate-loans.html': 'realEstate',
            'commercial-bridge-loans.html': 'bridge',
            'fix-and-flip.html': 'fixFlip',

            // SBA and business credit pages
            'sba-loans.html': 'sba',
            'business-line-of-credit.html': 'lineCredit',
            'business-term-loans.html': 'termLoans',
            'working-capital-loans.html': 'workingCapital',
            'working-capital.html': 'workingCapital',
            'revenue-based-financing.html': 'revenueBased',
            'securities-based-lending.html': 'securities',

            // Blog hub and blog posts
            'blog.html': 'blog',
            'sba-loans': 'sba',
            'sba-loans/articles': 'sba',
            'equipment-financing': 'equipment',
            'equipment-financing/articles': 'equipment',
            'business-line-of-credit': 'lineCredit',
            'business-line-of-credit/articles': 'lineCredit',
            'working-capital-loans': 'workingCapital',
            'working-capital-loans/articles': 'workingCapital',
            'business-term-loans': 'termLoans',
            'business-term-loans/articles': 'termLoans',
            'commercial-real-estate-loans': 'realEstate',
            'commercial-bridge-loans': 'bridge',
            'revenue-based-financing': 'revenueBased',
            'securities-based-lending': 'securities',
            'fix-and-flip': 'fixFlip',
            // Legacy -blog.html (redirect targets)
            'business-line-of-credit-blog.html': 'lineCredit',
            'business-term-loans-blog.html': 'termLoans',
            'commercial-bridge-loans-blog.html': 'bridge',
            'commercial-real-estate-loans-blog.html': 'realEstate',
            'equipment-financing-blog.html': 'equipment',
            'fix-and-flip-blog.html': 'fixFlip',
            'revenue-based-financing-blog.html': 'revenueBased',
            'sba-loans-blog.html': 'sba',
            'securities-based-lending-blog.html': 'securities',
            'working-capital-loans-blog.html': 'workingCapital'
        };

        const curatedKey = curatedPageSet[page];
        if (curatedKey && sets[curatedKey]) return sets[curatedKey];

        if (/equipment|excavator|dozer|dump-truck|trailer|skid-steer|manufacturing|medical|food-service|farm|cnc|bucket-truck|wood-chipper|same-day|no-doc|startup|used-equipment/.test(page)) {
            return sets.equipment;
        }
        if (/commercial-real-estate|real-estate|cre/.test(page)) return sets.realEstate;
        if (/sba/.test(page)) return sets.sba;
        if (/fix-and-flip|flip/.test(page)) return sets.fixFlip;
        if (/bridge/.test(page)) return sets.bridge;
        if (/business-line-of-credit|line-of-credit/.test(page)) return sets.lineCredit;
        if (/working-capital/.test(page)) return sets.workingCapital;
        if (/term-loans/.test(page)) return sets.termLoans;
        if (/revenue-based-financing/.test(page)) return sets.revenueBased;
        if (/securities-based-lending/.test(page)) return sets.securities;
        if (/blog/.test(page) || /\/blog\//.test(path)) return sets.blog;
        return sets.growth;
    }

    function buildTopicVisual(url, alt, variant, caption) {
        const figure = document.createElement('figure');
        figure.className = 'topic-visual topic-visual-' + (variant || 'inline');
        const img = document.createElement('img');
        img.src = url;
        img.alt = alt;
        img.loading = 'lazy';
        img.decoding = 'async';
        img.addEventListener('error', function() {
            // Remove broken remote images instead of showing broken placeholders.
            if (figure.parentElement) {
                figure.remove();
            }
        }, { once: true });
        figure.appendChild(img);
        if (caption) {
            const figcaption = document.createElement('figcaption');
            figcaption.textContent = caption;
            figure.appendChild(figcaption);
        }
        return figure;
    }

    function injectTopicVisuals() {
        const path = (window.location.pathname || '').toLowerCase();
        const page = path.split('/').pop() || 'index.html';
        const isIndustryPage = /(construction|trucking)-business-financing\.html$/.test(page);
        if (isIndustryPage) return;

        const visual = resolveVisualSet(getTopicVisualSet());
        const universalPool = getUniversalVisualPool();
        const pageTitle = (document.title || 'Axiant Partners').replace(/\s+\|.*$/, '').trim();
        const altBase = pageTitle || 'Business financing';
        const artDirection = getPageArtDirection(page);
        const isBlogPost = /\/blog\//.test(path) && page.endsWith('.html');
        const isBlogHub = !isBlogPost && /(^|-)blog\.html$/.test(page);
        const isServicePage = !isBlogPost && !isBlogHub && /(financing|loans|lending|capital|bridge|flip|sba|line-of-credit|term-loans)/.test(page);
        const usedUrls = new Set();
        const recentVisuals = isServicePage ? getRecentServiceVisuals() : null;
        const orderedCursors = { banner: 0, inline: 0, card: 0, mixed: 0 };
        const pickFromPool = function(poolName, seed) {
            const list = visual[poolName] || [];
            const scoped = list.length
                ? (artDirection ? pickVisualUrlOrdered(list, poolName, orderedCursors, usedUrls, recentVisuals) : pickVisualUrl(list, seed, usedUrls, recentVisuals))
                : '';
            if (scoped) return scoped;
            return pickVisualUrl(universalPool, seed + '-universal', usedUrls, null);
        };
        const intro = document.querySelector('.form-container .results-intro, .services-content .results-intro, .blog-content .results-intro');
        if (intro && intro.parentElement && !isServicePage && !isBlogHub && !isBlogPost && !intro.parentElement.querySelector('.topic-visual.topic-visual-banner')) {
            const bannerUrl = pickFromPool('banner', page + '-intro-banner');
            if (bannerUrl) intro.insertAdjacentElement('afterend', buildTopicVisual(bannerUrl, altBase + ' overview image', 'banner', visual.caption));
        }
        // Service pages: place one compact contextual image inside first content section instead of a large banner.
        if (isServicePage) {
            const textSections = Array.from(document.querySelectorAll('.form-container .about-section')).filter(function(section) {
                if (!section || section.querySelector('.topic-visual')) return false;
                if (section.querySelector(':scope > .service-card')) return false;
                const paragraphText = Array.from(section.querySelectorAll('p')).map(function(node) {
                    return node.textContent || '';
                }).join(' ').trim();
                return paragraphText.length > 260;
            });

            const placements = (artDirection && Array.isArray(artDirection.textSectionPlan) && artDirection.textSectionPlan.length)
                ? artDirection.textSectionPlan
                : [{ index: 0, variant: 'compact', pool: 'inline' }, { index: 1, variant: 'side', pool: 'inline' }, { index: 2, variant: 'side', pool: 'inline' }];

            placements.forEach(function(plan, idx) {
                const section = textSections[plan.index];
                if (!section || section.querySelector('.topic-visual')) return;
                const heading = section.querySelector('h2, h3');
                const headingText = heading ? heading.textContent.trim() : '';
                const poolName = plan.pool || (plan.variant === 'compact' ? 'inline' : 'card');
                const extraUrl = pickFromPool(poolName, page + '-section-' + idx + '-' + headingText);
                if (!extraUrl) return;
                const anchor = (plan.variant === 'side')
                    ? section.querySelector('h2 + p, h3 + p, p + p, p')
                    : section.querySelector('p + p, p, h2, h3');
                const caption = (plan.variant === 'compact' && artDirection && artDirection.sectionCaption) ? artDirection.sectionCaption : null;
                const media = buildTopicVisual(extraUrl, (headingText || altBase) + ' supporting image', plan.variant || 'side', caption);
                if (anchor) {
                    anchor.insertAdjacentElement('afterend', media);
                } else {
                    section.appendChild(media);
                }
            });
        } else if (!intro && !isBlogHub && !isBlogPost) {
            // Core pages without intro: add one banner near top content section.
            const firstSection = document.querySelector('.form-container.about-content .about-section, .form-container.services-content .about-section, .form-container[class*="-content"] .about-section');
            if (firstSection && !firstSection.querySelector('.topic-visual')) {
                const anchor = firstSection.querySelector('p, h2, h3');
                const fallbackBannerUrl = pickFromPool('banner', page + '-fallback-banner');
                if (fallbackBannerUrl) {
                    const media = buildTopicVisual(fallbackBannerUrl, altBase + ' overview image', 'banner', visual.caption);
                    if (anchor) {
                        anchor.insertAdjacentElement('afterend', media);
                    } else {
                        firstSection.appendChild(media);
                    }
                }
            }
        }

        // Keep service-card sections visually consistent: every peer card gets an image.
        document.querySelectorAll('.about-section').forEach(function(section) {
            const cards = Array.from(section.querySelectorAll(':scope > .service-card'));
            if (cards.length < 2) return;
            cards.forEach(function(card, idx) {
                if (card.querySelector('.topic-visual')) return;
                const cardTitle = card.querySelector('h3') ? card.querySelector('h3').textContent.trim() : '';
                const cardSeed = page + '-card-' + idx + '-' + (cardTitle || card.textContent.slice(0, 30));
                const cardUrl = pickFromPool('card', cardSeed) || pickFromPool('inline', cardSeed + '-inline');
                if (!cardUrl) return;
                const media = buildTopicVisual(cardUrl, (cardTitle || altBase) + ' supporting image', 'compact', null);
                const heading = card.querySelector('h3');
                if (heading) {
                    heading.insertAdjacentElement('afterend', media);
                } else {
                    card.insertAdjacentElement('afterbegin', media);
                }
            });
        });

        // Keep all instructional/program cards populated (e.g., 3-step boxes).
        document.querySelectorAll('.about-section, .blog-article-block').forEach(function(scope, scopeIdx) {
            const cards = Array.from(scope.querySelectorAll(':scope .step-card, :scope .benefit-card, :scope .leasing-option-card'));
            if (cards.length < 2) return;
            cards.forEach(function(card, cardIdx) {
                if (card.querySelector('.topic-visual')) return;
                const titleNode = card.querySelector('h3, h4');
                const cardTitle = titleNode ? titleNode.textContent.trim() : '';
                const seed = page + '-detail-card-' + scopeIdx + '-' + cardIdx + '-' + (cardTitle || card.textContent.slice(0, 28));
                const guidedPool = getGuidedCardImagePool(cardTitle);
                const cardUrl = guidedPool
                    ? (artDirection ? pickVisualUrlOrdered(guidedPool, 'guided-' + cardIdx, orderedCursors, usedUrls, recentVisuals) : pickVisualUrl(guidedPool, seed + '-guided', usedUrls, recentVisuals))
                    : (pickFromPool('card', seed) || pickFromPool('inline', seed + '-inline'));
                if (!cardUrl) return;
                const media = buildTopicVisual(cardUrl, (cardTitle || altBase) + ' supporting image', 'compact', null);
                if (titleNode) {
                    titleNode.insertAdjacentElement('afterend', media);
                } else {
                    card.insertAdjacentElement('afterbegin', media);
                }
            });
        });

        // Add lightweight images to blog listing cards for visual rhythm.
        if (isBlogHub) {
            const blogCards = Array.from(document.querySelectorAll('.blog-listing .blog-card, .blog-content .blog-card')).slice(0, 8);
            blogCards.forEach(function(card, idx) {
                if (card.querySelector('.topic-visual')) return;
                const variant = idx % 3 === 0 ? 'inline' : 'compact';
                const title = card.querySelector('h3') ? card.querySelector('h3').textContent.trim() : altBase;
                const blogCardUrl = pickFromPool('inline', page + '-blog-card-' + title + '-' + idx);
                if (!blogCardUrl) return;
                const media = buildTopicVisual(blogCardUrl, title + ' image', variant, null);
                card.insertBefore(media, card.firstChild);
            });
        }

        // Blog posts: keep imagery light (single contextual image) to avoid clutter.
        if (isBlogPost) {
            const articleBlocks = Array.from(document.querySelectorAll('.blog-post-main .blog-article-block, .form-container.blog-post-content .blog-article-block'));
            articleBlocks.slice(0, 1).forEach(function(block, idx) {
                if (block.querySelector('.topic-visual') || block.querySelector('img')) return;
                const h2 = block.querySelector('h2');
                const alt = (h2 ? h2.textContent.trim() : altBase) + ' image';
                const postUrl = pickFromPool('inline', page + '-post-block-' + idx + '-' + alt);
                if (!postUrl) return;
                block.appendChild(buildTopicVisual(postUrl, alt, 'side', null));
            });

            // Fallback for posts that do not get transformed into .blog-article-block sections.
            if (!document.querySelector('.form-container.blog-post-content .topic-visual')) {
                const container = document.querySelector('.form-container.blog-post-content');
                if (container) {
                    const anchor = container.querySelector('h2, p');
                    const fallbackUrl = pickFromPool('inline', page + '-post-fallback');
                    if (anchor && fallbackUrl) {
                        anchor.insertAdjacentElement('afterend', buildTopicVisual(fallbackUrl, altBase + ' image', 'compact', null));
                    }
                }
            }
        }

        if (recentVisuals) {
            saveRecentServiceVisuals(recentVisuals);
        }
    }

    function forceEnglish() {
        enforceAssetVersioning();
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
        ensureIndustriesMenuLinks();
        normalizeServiceMenuLinks();
        ensureReferralTab();
        injectMobileHardFixStyles();
        placeThemeToggleInMobileHeader();
        enhanceThemeToggle();
        enhanceMobileMenuBehavior();
        standardizeBrandLogos();
        syncLegacyFooterYear();
        enhanceGlobalFooter();
        injectAxelChatbot();

        // Run blog/media enhancements immediately so visuals always render.
        enhanceBlogPostLayout();
        enhanceIndustryPageLayout();
        injectTopicVisuals();

        // Defer only logo cleanup, which is non-critical for content rendering.
        if (window.requestIdleCallback) {
            window.requestIdleCallback(cleanAllWordmarkLogos, { timeout: 1500 });
        } else {
            window.setTimeout(cleanAllWordmarkLogos, 180);
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
