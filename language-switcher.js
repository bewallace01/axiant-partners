// Language Switcher for Axiant Partners Website
(function() {
    'use strict';

    // Get current language from localStorage or default to 'en'
    let currentLanguage = localStorage.getItem('language') || 'en';
    
    // Supported languages
    const supportedLanguages = {
        'en': 'English',
        'es': 'Español',
        'ru': 'Русский'
    };
    const servicePageNames = new Set(['sbaLoans', 'equipmentFinancing', 'businessLineOfCredit', 'workingCapitalLoans', 'businessTermLoans', 'commercialRealEstateLoans', 'commercialBridgeLoans', 'revenueBasedFinancing', 'fixAndFlip']);
    const originalTextMap = new WeakMap();
    const runtimeTranslationCache = {};


    // Initialize language switcher
    function initLanguageSwitcher() {
        console.log('Initializing language switcher');
        console.log('Theme toggle exists:', !!document.getElementById('themeToggle'));
        console.log('Nav links exists:', !!document.querySelector('.nav-links'));
        
        // Create language selector dropdown if it doesn't exist
        if (!document.getElementById('languageSelector')) {
            createLanguageSelector();
        } else {
            console.log('Language selector already exists in DOM');
        }
        
        // Load saved language preference
        setLanguage(currentLanguage);
        
        // Wait a tiny bit to ensure DOM is fully ready
        setTimeout(function() {
            translatePage();
        }, 100);
    }

    // Create language selector dropdown
    function createLanguageSelector() {
        console.log('Creating language selector...');
        
        const navLinks = document.querySelector('.nav-links');
        if (!navLinks) {
            console.error('Could not find .nav-links element');
            return;
        }
        
        // Check if selector already exists
        if (document.getElementById('languageSelector')) {
            console.log('Language selector already exists');
            return;
        }

        // Create language selector wrapper
        const langWrapper = document.createElement('div');
        langWrapper.className = 'language-selector-wrapper';
        
        // Create select element
        const select = document.createElement('select');
        select.id = 'languageSelector';
        select.className = 'language-selector';
        select.setAttribute('aria-label', 'Select language');
        
        // Add language options
        Object.keys(supportedLanguages).forEach(langCode => {
            const option = document.createElement('option');
            option.value = langCode;
            option.textContent = supportedLanguages[langCode];
            if (langCode === currentLanguage) {
                option.selected = true;
            }
            select.appendChild(option);
        });
        
        // Add change event listener
        select.addEventListener('change', function(e) {
            const newLang = e.target.value;
            setLanguage(newLang);
            translatePage();
        });
        
        langWrapper.appendChild(select);
        
        // Try to insert before theme toggle, otherwise append to navLinks
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            navLinks.insertBefore(langWrapper, themeToggle);
            console.log('Language selector inserted before theme toggle');
        } else {
            navLinks.appendChild(langWrapper);
            console.log('Theme toggle not found, appended language selector to nav links');
        }
    }

    // Set language and save to localStorage
    function setLanguage(lang) {
        currentLanguage = lang;
        localStorage.setItem('language', lang);
        
        // Update HTML lang attribute
        document.documentElement.setAttribute('lang', lang);
        
        // Update RTL for Arabic
        if (lang === 'ar') {
            document.documentElement.setAttribute('dir', 'rtl');
        } else {
            document.documentElement.setAttribute('dir', 'ltr');
        }
        
        // Update language selector if it exists
        const selector = document.getElementById('languageSelector');
        if (selector) {
            selector.value = lang;
        }

    }

    function normalizeText(s) {
        return s ? s.replace(/\s+/g, ' ').trim() : '';
    }

    function collectServiceTextNodes() {
        const container = document.querySelector('.form-container');
        if (!container) return [];
        const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null);
        const nodes = [];
        let n;
        while ((n = walker.nextNode())) {
            const raw = n.nodeValue || '';
            const normalized = normalizeText(raw);
            if (!normalized) continue;
            if (!originalTextMap.has(n)) originalTextMap.set(n, raw);
            nodes.push(n);
        }
        return nodes;
    }

    async function translateTextViaApi(text, targetLang) {
        const key = targetLang + '|' + text;
        if (runtimeTranslationCache[key]) return runtimeTranslationCache[key];

        const url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=' +
            encodeURIComponent(targetLang) + '&dt=t&q=' + encodeURIComponent(text);
        const response = await fetch(url);
        if (!response.ok) return text;
        const data = await response.json();
        let translated = '';
        if (Array.isArray(data) && Array.isArray(data[0])) {
            data[0].forEach(function(part) {
                if (Array.isArray(part) && part[0]) translated += part[0];
            });
        }
        translated = translated || text;
        runtimeTranslationCache[key] = translated;
        return translated;
    }

    async function applyRuntimeServiceBodyTranslation(pageName, lang) {
        if (!servicePageNames.has(pageName)) return;
        const nodes = collectServiceTextNodes();
        if (!nodes.length) return;

        if (lang === 'en') {
            nodes.forEach(function(node) {
                const original = originalTextMap.get(node);
                if (typeof original === 'string') node.nodeValue = original;
            });
            return;
        }

        const unique = new Set();
        const source = [];
        nodes.forEach(function(node) {
            const original = originalTextMap.get(node) || node.nodeValue || '';
            const normalized = normalizeText(original);
            if (!normalized || unique.has(normalized)) return;
            unique.add(normalized);
            source.push(normalized);
        });

        const translatedMap = {};
        const concurrency = 6;
        for (let i = 0; i < source.length; i += concurrency) {
            const slice = source.slice(i, i + concurrency);
            const results = await Promise.all(slice.map(function(item) {
                return translateTextViaApi(item, lang);
            }));
            slice.forEach(function(item, idx) {
                translatedMap[item] = results[idx] || item;
            });
        }

        nodes.forEach(function(node) {
            const original = originalTextMap.get(node) || node.nodeValue || '';
            const normalized = normalizeText(original);
            if (!normalized || !translatedMap[normalized]) return;
            const leading = (original.match(/^\s*/) || [''])[0];
            const trailing = (original.match(/\s*$/) || [''])[0];
            node.nodeValue = leading + translatedMap[normalized] + trailing;
        });
    }

    // Translate page content
    function translatePage() {
        console.log('Translating page, current language:', currentLanguage);
        
        if (typeof translations === 'undefined') {
            console.error('Translations object not found! Make sure translations.js is loaded before language-switcher.js');
            return;
        }
        
        if (!translations[currentLanguage]) {
            console.warn('Translations not available for language:', currentLanguage);
            return;
        }

        const t = translations[currentLanguage];
        console.log('Translation object loaded for:', currentLanguage);

        // Translate navigation
        translateNavigation(t);
        
        // Translate common elements
        translateCommon(t);
        
        // Translate page-specific content based on current page
        const pageName = getPageName();
        console.log('Current page name:', pageName);
        translatePageContent(pageName, t);
        applyRuntimeServiceBodyTranslation(pageName, currentLanguage);
        
        console.log('Translation complete');
    }

    // Get current page name
    function getPageName() {
        const path = window.location.pathname;
        const page = path.split('/').pop() || 'index.html';
        if (page.includes('index') || page === '') return 'home';
        if (page.includes('calculator')) return 'calculator';
        if (page.includes('match')) return 'match';
        if (page.includes('services')) return 'services';
        if (page === 'sba-loans.html') return 'sbaLoans';
        if (page === 'equipment-financing.html') return 'equipmentFinancing';
        if (page === 'business-line-of-credit.html') return 'businessLineOfCredit';
        if (page === 'working-capital-loans.html') return 'workingCapitalLoans';
        if (page === 'business-term-loans.html') return 'businessTermLoans';
        if (page === 'commercial-real-estate-loans.html') return 'commercialRealEstateLoans';
        if (page === 'commercial-bridge-loans.html') return 'commercialBridgeLoans';
        if (page === 'revenue-based-financing.html') return 'revenueBasedFinancing';
        if (page === 'fix-and-flip.html') return 'fixAndFlip';
        if (page === 'sba-loans-blog.html') return 'sbaLoansBlog';
        if (page === 'working-capital-loans-blog.html') return 'workingCapitalLoansBlog';
        if (page === 'business-term-loans-blog.html') return 'businessTermLoansBlog';
        if (page === 'commercial-real-estate-loans-blog.html') return 'commercialRealEstateLoansBlog';
        if (page === 'commercial-bridge-loans-blog.html') return 'commercialBridgeLoansBlog';
        if (page === 'revenue-based-financing-blog.html') return 'revenueBasedFinancingBlog';
        if (page === 'equipment-financing-blog.html') return 'equipmentFinancingBlog';
        if (page === 'business-line-of-credit-blog.html') return 'businessLineOfCreditBlog';
        if (page === 'fix-and-flip-blog.html') return 'fixAndFlipBlog';
        if (page === 'sba-7a-vs-504-loan.html') return 'sba7aVs504LoanPost';
        if (page === 'what-credit-score-needed-sba-loan.html') return 'whatCreditScoreNeededSbaLoanPost';
        if (page === 'how-long-sba-loan-approval.html') return 'howLongSbaLoanApprovalPost';
        if (page === 'what-credit-score-needed-equipment-financing.html') return 'whatCreditScoreNeededEquipmentFinancingPost';
        if (page === 'what-benefits-does-lease-have-equipment-financing.html') return 'leaseBenefitsEquipmentFinancingPost';
        if (page === 'equipment-leasing-vs-loan-which-is-better.html') return 'equipmentLeasingVsLoanPost';
        if (page === 'business-line-of-credit-vs-term-loan.html') return 'businessLineOfCreditVsTermLoanPost';
        if (page === 'what-credit-score-needed-business-line-of-credit.html') return 'whatCreditScoreNeededBusinessLineOfCreditPost';
        if (page === 'do-you-need-collateral-business-line-of-credit.html') return 'collateralBusinessLineOfCreditPost';
        if (page === 'how-much-down-payment-fix-and-flip-loan.html') return 'fixAndFlipDownPaymentPost';
        if (page === 'what-credit-score-needed-fix-and-flip-loan.html') return 'whatCreditScoreNeededFixAndFlipPost';
        if (page === 'typical-fix-and-flip-loan-rates.html') return 'typicalFixAndFlipLoanRatesPost';
        if (page === 'what-is-working-capital-loan-how-does-it-work.html') return 'whatIsWorkingCapitalLoanPost';
        if (page === 'working-capital-loan-vs-business-line-of-credit.html') return 'workingCapitalVsLineOfCreditPost';
        if (page === 'what-credit-score-needed-working-capital-loan.html') return 'whatCreditScoreNeededWorkingCapitalPost';
        if (page === 'what-credit-score-needed-business-term-loan.html') return 'whatCreditScoreNeededBusinessTermLoanPost';
        if (page === 'business-term-loan-vs-line-of-credit.html') return 'businessTermLoanVsLineOfCreditPost';
        if (page === 'what-do-lenders-look-for-business-term-loan.html') return 'whatLendersLookForBusinessTermLoanPost';
        if (page === 'what-credit-score-needed-commercial-real-estate-loan.html') return 'whatCreditScoreNeededCommercialRealEstatePost';
        if (page === 'how-much-down-payment-required-commercial-property-loan.html') return 'howMuchDownPaymentCommercialPropertyPost';
        if (page === 'what-do-lenders-look-for-commercial-real-estate-loan.html') return 'whatLendersLookForCommercialRealEstatePost';
        if (page === 'when-should-you-use-commercial-bridge-loan.html') return 'whenShouldUseCommercialBridgeLoanPost';
        if (page === 'how-fast-can-you-close-commercial-bridge-loan.html') return 'howFastCloseCommercialBridgeLoanPost';
        if (page === 'what-do-lenders-look-for-commercial-bridge-loan.html') return 'whatLendersLookForCommercialBridgeLoanPost';
        if (page === 'what-is-revenue-based-financing-how-does-it-work.html') return 'whatIsRevenueBasedFinancingPost';
        if (page === 'revenue-based-financing-vs-merchant-cash-advance.html') return 'revenueBasedVsMcaPost';
        if (page === 'what-credit-score-needed-revenue-based-financing.html') return 'whatCreditScoreNeededRevenueBasedPost';
        if (page.includes('faq')) return 'faq';
        if (page.includes('contact')) return 'contact';
        if (page === 'blog.html') return 'blog';
        if (page.includes('glossary')) return 'glossary';
        
        return 'home';
    }

    // Translate navigation
    function translateNavigation(t) {
        if (!t || !t.nav) {
            console.log('No navigation translations available');
            return;
        }
        
        console.log('Translating navigation...');
        
        // Find all nav links by their href
        const navLinks = {
            'index.html': t.nav.about,
            'match.html': t.nav.findMatch,
            'sba-loans.html': t.nav.sbaLoans,
            'equipment-financing.html': t.nav.equipmentFinancing,
            'business-line-of-credit.html': t.nav.businessLineOfCredit,
            'working-capital-loans.html': t.nav.workingCapitalLoans,
            'business-term-loans.html': t.nav.businessTermLoans,
            'commercial-real-estate-loans.html': t.nav.commercialRealEstateLoans,
            'commercial-bridge-loans.html': t.nav.commercialBridgeLoans,
            'revenue-based-financing.html': t.nav.revenueBasedFinancing,
            'fix-and-flip.html': t.nav.fixAndFlip,
            'services.html': t.nav.services,
            'faq.html': t.nav.faq,
            'contact.html': t.nav.contact,
            'blog.html': t.nav.blog,
            'glossary.html': t.nav.glossary
        };
        
        const links = document.querySelectorAll('.nav-links a');
        console.log('Found', links.length, 'navigation links');
        
        links.forEach(link => {
            const href = link.getAttribute('href');
            const key = href ? href.split('/').pop() : '';
            if (key && navLinks[key]) {
                console.log('Translating link:', href, 'to:', navLinks[key]);
                link.textContent = navLinks[key];
            }
        });

        // Translate Services dropdown trigger text (button, not anchor).
        const servicesTrigger = document.querySelector('.nav-dropdown-trigger');
        if (servicesTrigger && t.nav.services) {
            servicesTrigger.textContent = t.nav.services;
        }

        // Ensure newly added service pages appear in every dropdown (root + blog paths).
        function ensureServiceMenuLink(fileName, label) {
            document.querySelectorAll('.nav-dropdown-menu').forEach(function(menu) {
                const existing = menu.querySelector('a[href$="' + fileName + '"]');
                if (existing) {
                    if (label) existing.textContent = label;
                    return;
                }
                const refLink = menu.querySelector('a[href$="sba-loans.html"]') || menu.querySelector('a');
                const refHref = refLink ? (refLink.getAttribute('href') || '') : '';
                const prefix = refHref.startsWith('../') ? '../' : '';
                const newLink = document.createElement('a');
                newLink.setAttribute('href', prefix + fileName);
                newLink.textContent = label || '';
                const beforeNode = menu.querySelector('a[href$="fix-and-flip.html"]');
                if (beforeNode) {
                    menu.insertBefore(newLink, beforeNode);
                } else {
                    menu.appendChild(newLink);
                }
            });
        }

        ensureServiceMenuLink('commercial-real-estate-loans.html', t.nav.commercialRealEstateLoans || 'Commercial Real Estate Loans');
        ensureServiceMenuLink('commercial-bridge-loans.html', t.nav.commercialBridgeLoans || 'Commercial Bridge Loans');
        ensureServiceMenuLink('revenue-based-financing.html', t.nav.revenueBasedFinancing || 'Revenue-Based Financing');

        // Force-translate services submenu labels for any path variant.
        const forceMap = {
            'sba-loans.html': t.nav.sbaLoans,
            'equipment-financing.html': t.nav.equipmentFinancing,
            'business-line-of-credit.html': t.nav.businessLineOfCredit,
            'working-capital-loans.html': t.nav.workingCapitalLoans,
            'business-term-loans.html': t.nav.businessTermLoans,
            'commercial-real-estate-loans.html': t.nav.commercialRealEstateLoans,
            'commercial-bridge-loans.html': t.nav.commercialBridgeLoans,
            'revenue-based-financing.html': t.nav.revenueBasedFinancing,
            'fix-and-flip.html': t.nav.fixAndFlip
        };
        Object.keys(forceMap).forEach(function(file) {
            const label = forceMap[file];
            if (!label) return;
            document.querySelectorAll('.nav-dropdown-menu a[href$="' + file + '"]').forEach(function(a) {
                a.textContent = label;
            });
        });
    }

    // Translate common elements (footer, buttons, etc.)
    function translateCommon(t) {
        if (!t.common) return;
        
        // Footer
        const footer = document.querySelector('.site-footer p');
        if (footer && t.common.footerText) {
            const privacyLink = footer.querySelector('a[href*="privacy"]');
            const termsLink = footer.querySelector('a[href*="terms"]');
            if (privacyLink) privacyLink.textContent = t.common.privacyPolicy;
            if (termsLink) termsLink.textContent = t.common.termsConditions;
        }
        
        // Common buttons
        document.querySelectorAll('.btn-primary').forEach(btn => {
            const text = btn.textContent.trim();
            if (text === 'Get Started Now' && t.common.getStarted) {
                btn.textContent = t.common.getStarted;
            }
        });
    }

    // Translate page-specific content
    function translatePageContent(pageName, t) {
        // Fallback to English if current language doesn't have complete translations
        const pageT = t && t[pageName] ? t[pageName] : null;
        const englishT = translations['en'] && translations['en'][pageName] ? translations['en'][pageName] : null;
        
        if (!pageT && !englishT) {
            console.log('No translations found for page:', pageName);
            return;
        }
        
        // Helper function to get translation with fallback
        function getTranslation(key) {
            return (pageT && pageT[key]) ? pageT[key] : ((englishT && englishT[key]) ? englishT[key] : null);
        }
        
        // Update page title and tagline (skip for blog posts - they keep their article-specific titles)
        if (pageName !== 'blogPost') {
            const h1 = document.querySelector('header h1');
            const tagline = document.querySelector('header .tagline');
            
            const pageTitle = pageT && pageT.title ? pageT.title : (englishT && englishT.title ? englishT.title : null);
            if (h1 && pageTitle) {
                h1.textContent = pageTitle;
                document.title = pageTitle + ' - Axiant Partners';
            }
            
            const pageTagline = pageT && pageT.tagline ? pageT.tagline : (englishT && englishT.tagline ? englishT.tagline : null);
            if (tagline && pageTagline) {
                tagline.textContent = pageTagline;
            }
        }
        
        // Home page specific translations - use index-based selection instead of text matching
        if (pageName === 'home') {
            const sections = document.querySelectorAll('.about-section');
            
            // Section 0: "What We Do"
            if (sections[0]) {
                const h2 = sections[0].querySelector('h2');
                const whatWeDo = getTranslation('whatWeDo');
                if (h2 && whatWeDo) h2.textContent = whatWeDo;
                
                const paragraphs = sections[0].querySelectorAll('p');
                const text1 = getTranslation('whatWeDoText1');
                const text2 = getTranslation('whatWeDoText2');
                if (paragraphs.length >= 1 && text1) paragraphs[0].textContent = text1;
                if (paragraphs.length >= 2 && text2) paragraphs[1].textContent = text2;
            }
            
            // Section 1: "How It Works"
            if (sections[1]) {
                const h2 = sections[1].querySelector('h2');
                const howItWorks = getTranslation('howItWorks');
                if (h2 && howItWorks) h2.textContent = howItWorks;
                
                const cards = sections[1].querySelectorAll('.step-card');
                const steps = [
                    { title: getTranslation('step1Title'), text: getTranslation('step1Text') },
                    { title: getTranslation('step2Title'), text: getTranslation('step2Text') },
                    { title: getTranslation('step3Title'), text: getTranslation('step3Text') },
                    { title: getTranslation('step4Title'), text: getTranslation('step4Text') }
                ];
                cards.forEach((card, index) => {
                    if (steps[index] && steps[index].title) {
                        const h3 = card.querySelector('h3');
                        const p = card.querySelector('p');
                        if (h3 && steps[index].title) h3.textContent = steps[index].title;
                        if (p && steps[index].text) p.textContent = steps[index].text;
                    }
                });
            }
            
            // Section 2: "Why Choose Axiant Partners"
            if (sections[2]) {
                const h2 = sections[2].querySelector('h2');
                const whyChoose = getTranslation('whyChoose');
                if (h2 && whyChoose) h2.textContent = whyChoose;
                
                const cards = sections[2].querySelectorAll('.benefit-card');
                const benefits = [
                    { title: getTranslation('benefit1Title'), text: getTranslation('benefit1Text') },
                    { title: getTranslation('benefit2Title'), text: getTranslation('benefit2Text') },
                    { title: getTranslation('benefit3Title'), text: getTranslation('benefit3Text') },
                    { title: getTranslation('benefit4Title'), text: getTranslation('benefit4Text') },
                    { title: getTranslation('benefit5Title'), text: getTranslation('benefit5Text') },
                    { title: getTranslation('benefit6Title'), text: getTranslation('benefit6Text') }
                ];
                cards.forEach((card, index) => {
                    if (benefits[index] && benefits[index].title) {
                        const h3 = card.querySelector('h3');
                        const p = card.querySelector('p');
                        if (h3 && benefits[index].title) h3.textContent = benefits[index].title;
                        if (p && benefits[index].text) p.textContent = benefits[index].text;
                    }
                });
            }
            
            // Section 3: "Our Lending Partners"
            if (sections[3]) {
                const h2 = sections[3].querySelector('h2');
                const lendingPartners = getTranslation('lendingPartners');
                if (h2 && lendingPartners) h2.textContent = lendingPartners;
                
                const paragraphs = sections[3].querySelectorAll('p');
                const lendingText = getTranslation('lendingPartnersText');
                if (paragraphs.length >= 1 && lendingText) {
                    paragraphs[0].textContent = lendingText.replace(/<strong>.*?<\/strong>/g, '').replace(/<strong>/g, '').replace(/<\/strong>/g, '');
                }
                const partnerTypes = getTranslation('partnerTypes');
                if (paragraphs.length >= 2 && partnerTypes) {
                    paragraphs[1].textContent = partnerTypes;
                }
                
                const list = sections[3].querySelector('ul.partner-list');
                if (list) {
                    const items = list.querySelectorAll('li');
                    const partnerType1 = getTranslation('partnerType1');
                    const partnerType2 = getTranslation('partnerType2');
                    const partnerType3 = getTranslation('partnerType3');
                    const partnerType4 = getTranslation('partnerType4');
                    const partnerType5 = getTranslation('partnerType5');
                    const partnerType6 = getTranslation('partnerType6');
                    if (items.length >= 1 && partnerType1) items[0].textContent = partnerType1;
                    if (items.length >= 2 && partnerType2) items[1].textContent = partnerType2;
                    if (items.length >= 3 && partnerType3) items[2].textContent = partnerType3;
                    if (items.length >= 4 && partnerType4) items[3].textContent = partnerType4;
                    if (items.length >= 5 && partnerType5) items[4].textContent = partnerType5;
                    if (items.length >= 6 && partnerType6) items[5].textContent = partnerType6;
                }
            }
            
            // Section 4: "Ready to Get Connected" CTA
            if (sections[4]) {
                const h2 = sections[4].querySelector('h2');
                const readyToConnect = getTranslation('readyToConnect');
                if (h2 && readyToConnect) h2.textContent = readyToConnect;
                
                const p = sections[4].querySelector('p');
                const readyText = getTranslation('readyToConnectText');
                if (p && readyText) p.textContent = readyText;
                
                const btn = sections[4].querySelector('.btn-primary');
                const getStarted = t.common && t.common.getStarted ? t.common.getStarted : (translations['en'] && translations['en'].common ? translations['en'].common.getStarted : null);
                if (btn && getStarted) btn.textContent = getStarted;
            }
        }
        
        // Match page translations
        if (pageName === 'match' && pageT.formTitle) {
            const formTitle = document.querySelector('.form-container h2');
            if (formTitle && pageT.formTitle) {
                formTitle.textContent = pageT.formTitle;
            }
            const formIntro = document.querySelector('.results-intro');
            if (formIntro && pageT.formIntro) {
                formIntro.textContent = pageT.formIntro;
            }
            
            // Translate form labels
            translateFormLabels(pageT);
        }
        
        // Services page translations
        if (pageName === 'services') {
            const sectionTitle = document.querySelector('.services-content h2');
            const title = getTranslation('sectionTitle');
            if (sectionTitle && title) sectionTitle.textContent = title;
            
            const sectionIntro = document.querySelector('.services-content .results-intro');
            const intro = getTranslation('sectionIntro');
            if (sectionIntro && intro) sectionIntro.textContent = intro;
            
            // Translate service cards
            const serviceCards = document.querySelectorAll('.services-grid .service-card');
            const services = [];
            for (let i = 1; i <= 20; i++) {
                const titleKey = 'service' + i + 'Title';
                const textKey = 'service' + i + 'Text';
                const title = getTranslation(titleKey);
                const text = getTranslation(textKey);
                if (title || text) {
                    services.push({ title: title, text: text });
                }
            }
            
            serviceCards.forEach((card, index) => {
                if (services[index]) {
                    const h3 = card.querySelector('h3');
                    const p = card.querySelector('p');
                    if (h3 && services[index].title) h3.textContent = services[index].title;
                    if (p && services[index].text) p.textContent = services[index].text;
                }
            });
            
            // Translate CTA section
            const ctaSection = document.querySelector('.services-cta');
            if (ctaSection) {
                const ctaTitle = getTranslation('ctaTitle');
                const ctaText = getTranslation('ctaText');
                const ctaH3 = ctaSection.querySelector('h3');
                const ctaP = ctaSection.querySelector('p');
                const ctaBtn = ctaSection.querySelector('.btn-primary');
                if (ctaH3 && ctaTitle) ctaH3.textContent = ctaTitle;
                if (ctaP && ctaText) ctaP.textContent = ctaText;
                const getStarted = t.common && t.common.getStarted ? t.common.getStarted : (translations['en'] && translations['en'].common ? translations['en'].common.getStarted : null);
                if (ctaBtn && getStarted) ctaBtn.textContent = getStarted;
            }
        }

        // Topic blog listing pages (e.g. working-capital-loans-blog.html)
        if (pageName.endsWith('Blog')) {
            translateBlogListing(pageT, t.common, getTranslation);
        }
        
        // FAQ page translations
        if (pageName === 'faq') {
            translateFAQ(pageT, englishT, function(key) {
                return getTranslation(key);
            });
        }
        
        // Contact page translations
        if (pageName === 'contact' && pageT.getInTouch) {
            translateContact(pageT, t.common);
        }
        
        // Calculator page - title and tagline are already handled above in the general section
        // No additional content to translate for calculator page
    }

    // Helper function removed - now using index-based translation directly

    // Translate form labels on match page
    function translateFormLabels(t) {
        const labels = {
            'Full Name': t.fullName,
            'Email Address': t.email,
            'Phone Number': t.phone,
            'Loan Amount ($)': t.loanAmount,
            'Business Name': t.businessName,
            'Business Loan Type': t.loanType,
            'Credit Score': t.creditScore,
            'Annual Business Revenue ($)': t.revenue,
            'Years in Business': t.yearsInBusiness,
            'Equipment Being Financed (if applicable)': t.equipmentDescription
        };
        
        document.querySelectorAll('.form-group label').forEach(label => {
            const text = label.textContent.trim();
            if (labels[text]) {
                label.textContent = labels[text];
            }
        });
        
        // Translate select placeholders
        document.querySelectorAll('.form-group select option').forEach(option => {
            const text = option.textContent.trim();
            if (text === 'Select loan type' && t.selectLoanType) {
                option.textContent = t.selectLoanType;
            } else if (text === 'Select your credit score range' && t.selectCreditScore) {
                option.textContent = t.selectCreditScore;
            } else if (text === 'Select revenue range' && t.selectRevenue) {
                option.textContent = t.selectRevenue;
            } else if (text === 'Select years in business' && t.selectYears) {
                option.textContent = t.selectYears;
            }
        });
        
        // Translate button
        const submitBtn = document.querySelector('#loanForm button[type="submit"]');
        if (submitBtn && t.submitApplication) {
            submitBtn.textContent = t.submitApplication;
        }
    }

    // Translate FAQ items - use index-based selection
    function translateFAQ(pageT, englishT, getTranslation) {
        const questions = document.querySelectorAll('.faq-question');
        const qaPairs = [];
        for (let i = 1; i <= 12; i++) {
            const qKey = 'q' + i;
            const aKey = 'a' + i;
            const q = getTranslation ? getTranslation(qKey) : (pageT && pageT[qKey] ? pageT[qKey] : (englishT && englishT[qKey] ? englishT[qKey] : null));
            const a = getTranslation ? getTranslation(aKey) : (pageT && pageT[aKey] ? pageT[aKey] : (englishT && englishT[aKey] ? englishT[aKey] : null));
            if (q || a) {
                qaPairs.push({ q: q, a: a });
            }
        }
        
        questions.forEach((question, index) => {
            if (qaPairs[index] && qaPairs[index].q) {
                question.textContent = qaPairs[index].q;
                const answer = question.parentElement.querySelector('.faq-answer p');
                if (answer && qaPairs[index].a) {
                    answer.textContent = qaPairs[index].a;
                }
            }
        });
        
        // Translate CTA section
        const ctaTitle = document.querySelector('.faq-cta h2');
        const ctaText = document.querySelector('.faq-cta p');
        const ctaBtn = document.querySelector('.faq-cta .btn-primary');
        const stillHaveQuestions = getTranslation ? getTranslation('stillHaveQuestions') : (pageT && pageT.stillHaveQuestions ? pageT.stillHaveQuestions : (englishT && englishT.stillHaveQuestions ? englishT.stillHaveQuestions : null));
        const stillHaveQuestionsText = getTranslation ? getTranslation('stillHaveQuestionsText') : (pageT && pageT.stillHaveQuestionsText ? pageT.stillHaveQuestionsText : (englishT && englishT.stillHaveQuestionsText ? englishT.stillHaveQuestionsText : null));
        if (ctaTitle && stillHaveQuestions) ctaTitle.textContent = stillHaveQuestions;
        if (ctaText && stillHaveQuestionsText) ctaText.textContent = stillHaveQuestionsText;
        const getStarted = translations[currentLanguage] && translations[currentLanguage].common && translations[currentLanguage].common.getStarted ? translations[currentLanguage].common.getStarted : (translations['en'] && translations['en'].common ? translations['en'].common.getStarted : null);
        if (ctaBtn && getStarted) ctaBtn.textContent = getStarted;
    }

    // Translate topic blog listing pages
    function translateBlogListing(pageT, commonT, getTranslation) {
        if (!pageT) return;

        const backLink = document.querySelector('.blog-back a');
        const backText = getTranslation('backToAllBlogs');
        if (backLink && backText) backLink.textContent = backText;

        const intro = document.querySelector('.blog-listing .results-intro');
        const introText = getTranslation('listingIntro');
        if (intro && introText) intro.textContent = introText;

        const cards = document.querySelectorAll('.blog-listing .blog-card');
        cards.forEach((card, index) => {
            const title = getTranslation('post' + (index + 1) + 'Title');
            const excerpt = getTranslation('post' + (index + 1) + 'Excerpt');
            const readMore = getTranslation('readMore');

            const h3Link = card.querySelector('.blog-card-title a');
            const excerptP = card.querySelector('.blog-card-excerpt');
            const readMoreLink = card.querySelector('.blog-card-link');

            if (h3Link && title) h3Link.textContent = title;
            if (excerptP && excerpt) excerptP.textContent = excerpt;
            if (readMoreLink && readMore) readMoreLink.textContent = readMore;
        });

        const cta = document.querySelector('.blog-listing .services-cta');
        if (cta) {
            const ctaTitle = getTranslation('ctaTitle');
            const ctaText = getTranslation('ctaText');
            const ctaBtn = cta.querySelector('.btn-primary');
            const ctaH3 = cta.querySelector('h3');
            const ctaP = cta.querySelector('p');
            const getStarted = commonT && commonT.getStarted ? commonT.getStarted : null;

            if (ctaH3 && ctaTitle) ctaH3.textContent = ctaTitle;
            if (ctaP && ctaText) ctaP.textContent = ctaText;
            if (ctaBtn && getStarted) ctaBtn.textContent = getStarted;
        }
    }

    // Translate contact page
    function translateContact(t, common) {
        const getInTouch = document.querySelector('.contact-content h2');
        const getInTouchText = document.querySelector('.contact-content .results-intro');
        if (getInTouch && t.getInTouch) getInTouch.textContent = t.getInTouch;
        if (getInTouchText && t.getInTouchText) getInTouchText.textContent = t.getInTouchText;
        
        // Translate form labels
        const contactLabels = {
            'Full Name': t.fullName,
            'Email Address': t.email,
            'Phone Number': t.phone,
            'Subject': t.subject,
            'Message': t.message
        };
        
        document.querySelectorAll('.contact-form .form-group label').forEach(label => {
            const text = label.textContent.trim();
            if (contactLabels[text]) {
                label.textContent = contactLabels[text];
            }
        });
        
        // Translate buttons
        const sendBtn = document.querySelector('#contactForm button[type="submit"]');
        if (sendBtn && t.sendMessage) sendBtn.textContent = t.sendMessage;
        
        // Translate contact info section
        const otherWays = document.querySelector('.contact-info-section h3');
        if (otherWays && t.otherWays) otherWays.textContent = t.otherWays;
        
        const infoCards = document.querySelectorAll('.contact-info-card h4');
        if (infoCards.length >= 1 && t.emailLabel) infoCards[0].textContent = t.emailLabel;
        if (infoCards.length >= 2 && t.phoneLabel) infoCards[1].textContent = t.phoneLabel;
        if (infoCards.length >= 3 && t.businessHours) infoCards[2].textContent = t.businessHours;
    }

    // Initialize when DOM is ready
    function startLanguageSwitcher() {
        console.log('startLanguageSwitcher called, translations defined:', typeof translations !== 'undefined');
        
        // Wait for translations to be loaded
        if (typeof translations === 'undefined') {
            console.log('Waiting for translations.js to load...');
            setTimeout(startLanguageSwitcher, 100);
            return;
        }
        console.log('Translations loaded, initializing language switcher');
        initLanguageSwitcher();
    }
    
    // Start immediately - scripts load in order so translations.js should be loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            console.log('DOMContentLoaded event fired');
            startLanguageSwitcher();
        });
    } else {
        console.log('DOM already ready, starting language switcher immediately');
        // Give it a moment for translations.js to load
        setTimeout(startLanguageSwitcher, 50);
    }
    
    // Also try on window load as backup
    window.addEventListener('load', function() {
        console.log('Window load event fired');
        if (!document.getElementById('languageSelector')) {
            console.log('Language selector still not found on window load, retrying...');
            startLanguageSwitcher();
        }
    });

    // Export functions for external use
    window.languageSwitcher = {
        setLanguage: setLanguage,
        getLanguage: function() { return currentLanguage; },
        translatePage: translatePage
    };

})();
