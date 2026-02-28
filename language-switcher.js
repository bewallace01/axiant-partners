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
        const version = '20260307';
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
            if (!clean.endsWith('script.js')) return;
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

        document.querySelectorAll('.nav-dropdown-menu').forEach(function(menu) {
            const existing = new Map();
            menu.querySelectorAll('a').forEach(function(link) {
                const href = (link.getAttribute('href') || '').split('#')[0].split('?')[0];
                const file = href.split('/').pop();
                if (!file || existing.has(file)) return;
                existing.set(file, link);
            });

            menu.innerHTML = '';
            const prefix = getPathPrefix();
            serviceLinks.forEach(function(item) {
                const a = document.createElement('a');
                a.setAttribute('href', prefix + item.file);
                a.textContent = item.label;
                menu.appendChild(a);
            });
        });
    }

    function normalizeServiceMenuLinks() {
        document.querySelectorAll('.nav-dropdown-menu a').forEach(function(link) {
            const href = link.getAttribute('href') || '';
            if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
                return;
            }
            const file = href.split('?')[0].split('#')[0].split('/').pop();
            if (!file || !file.endsWith('.html')) return;
            const prefix = getPathPrefix();
            link.setAttribute('href', prefix + file);
        });
    }

    function ensureReferralTab() {
        const prefix = getPathPrefix();
        const onReferralPage = /\/referral\.html$/i.test(window.location.pathname || '');

        document.querySelectorAll('.nav-links').forEach(function(navLinks) {
            if (!navLinks) return;

            let referralLink = navLinks.querySelector('a[href$="referral.html"]');
            if (!referralLink) {
                referralLink = document.createElement('a');
                referralLink.setAttribute('href', prefix + 'referral.html');
                referralLink.textContent = 'Referral';
            }

            if (onReferralPage) {
                referralLink.classList.add('active');
            } else {
                referralLink.classList.remove('active');
            }

            const contactLink = navLinks.querySelector('a[href$="contact.html"]');
            if (contactLink && contactLink.parentElement === navLinks) {
                if (contactLink.nextSibling !== referralLink) {
                    contactLink.insertAdjacentElement('afterend', referralLink);
                }
            } else {
                const themeToggle = navLinks.querySelector('.theme-toggle');
                if (themeToggle) {
                    navLinks.insertBefore(referralLink, themeToggle);
                } else {
                    navLinks.appendChild(referralLink);
                }
            }
        });
    }

    function placeThemeToggleInMobileHeader() {
        // Keep theme toggle in the original nav-links container.
        // Moving the control between containers caused inconsistent tap behavior on some mobile browsers.
        return;
    }

    function injectMobileHardFixStyles() {
        const style = document.getElementById('mobileHardFixStyles');
        if (style) style.remove();
    }

    function enhanceThemeToggle() {
        const root = document.documentElement;
        const savedTheme = localStorage.getItem('theme');
        root.setAttribute('data-theme', savedTheme === 'dark' ? 'dark' : 'light');
        const toggle = document.getElementById('themeToggle') || document.querySelector('.theme-toggle');
        if (!toggle || toggle.dataset.themeEnhanced === '1') return;
        toggle.dataset.themeEnhanced = '1';
        toggle.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark' ? 'true' : 'false');
        toggle.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            const nextTheme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            root.setAttribute('data-theme', nextTheme);
            localStorage.setItem('theme', nextTheme);
            toggle.setAttribute('aria-pressed', nextTheme === 'dark' ? 'true' : 'false');
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
                        '<a href="' + prefix + 'business-term-loans.html">Business Term Loans</a>' +
                        '<a href="' + prefix + 'commercial-real-estate-loans.html">Commercial Real Estate</a>' +
                        '<a href="' + prefix + 'commercial-bridge-loans.html">Commercial Bridge Loans</a>' +
                        '<a href="' + prefix + 'revenue-based-financing.html">Revenue-Based Financing</a>' +
                        '<a href="' + prefix + 'securities-based-lending.html">Securities-Based Lending</a>' +
                        '<a href="' + prefix + 'fix-and-flip.html">Fix and Flip</a>' +
                    '</div>' +
                    '<div class="footer-col">' +
                        '<h4>Company</h4>' +
                        '<a href="' + prefix + 'index.html">About Us</a>' +
                        '<a href="' + prefix + 'contact.html">Contact</a>' +
                        '<a href="' + prefix + 'faq.html">FAQ</a>' +
                        '<a href="' + prefix + 'vendors.html">Vendors</a>' +
                        '<div class="footer-social">' +
                            '<h4>Follow Us</h4>' +
                            '<a href="https://www.linkedin.com/company/axiantpartners/" target="_blank" rel="noopener noreferrer">LinkedIn</a>' +
                            '<a href="https://www.facebook.com/share/1j27PpAoUS/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer">Facebook</a>' +
                            '<a href="https://www.instagram.com/axiantpartners?igsh=a25pcmZ3NGpxb3Fl&utm_source=qr" target="_blank" rel="noopener noreferrer">Instagram</a>' +
                        '</div>' +
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

    function injectAxelChatbot() {
        if (document.getElementById('axelChatLauncher')) return;
        const prefix = getPathPrefix();
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
                    '<img class="axel-chat-avatar" src="' + prefix + 'axel-loan-lion.png" alt="Axel the Loan Lion">' +
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
