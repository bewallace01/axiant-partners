// Bank database with lending criteria
const banks = [
    {
        name: "Prime National Bank",
        minCreditScore: "excellent",
        minIncome: 60000,
        loanTypes: ["personal", "home", "auto"],
        maxLoanAmount: 500000,
        employmentRequired: ["fulltime", "selfemployed"],
        approvalRate: 95,
        interestRate: "3.5% - 5.5%",
        features: ["Low interest rates", "Fast approval (24-48 hours)", "No prepayment penalty"]
    },
    {
        name: "Community First Credit Union",
        minCreditScore: "good",
        minIncome: 40000,
        loanTypes: ["personal", "auto", "home"],
        maxLoanAmount: 300000,
        employmentRequired: ["fulltime", "parttime", "selfemployed"],
        approvalRate: 85,
        interestRate: "4.5% - 7.0%",
        features: ["Member-focused service", "Flexible terms", "Lower fees"]
    },
    {
        name: "Business Growth Bank",
        minCreditScore: "good",
        minIncome: 50000,
        loanTypes: ["business", "personal"],
        maxLoanAmount: 1000000,
        employmentRequired: ["selfemployed", "fulltime"],
        approvalRate: 80,
        interestRate: "5.0% - 8.0%",
        features: ["Business expertise", "SBA loan options", "Business consulting included"]
    },
    {
        name: "Metro Trust Bank",
        minCreditScore: "fair",
        minIncome: 35000,
        loanTypes: ["personal", "auto", "home"],
        maxLoanAmount: 250000,
        employmentRequired: ["fulltime", "parttime", "selfemployed", "retired"],
        approvalRate: 75,
        interestRate: "6.0% - 9.5%",
        features: ["Accepts fair credit", "Multiple loan options", "Online application"]
    },
    {
        name: "SecondChance Financial",
        minCreditScore: "poor",
        minIncome: 25000,
        loanTypes: ["personal", "auto"],
        maxLoanAmount: 50000,
        employmentRequired: ["fulltime", "parttime", "selfemployed"],
        approvalRate: 70,
        interestRate: "8.5% - 14.0%",
        features: ["Bad credit accepted", "Credit building programs", "Financial counseling"]
    },
    {
        name: "Education First Bank",
        minCreditScore: "fair",
        minIncome: 0,
        loanTypes: ["student"],
        maxLoanAmount: 150000,
        employmentRequired: ["fulltime", "parttime", "selfemployed", "unemployed"],
        approvalRate: 90,
        interestRate: "4.0% - 7.5%",
        features: ["Student-focused", "Deferred payment options", "Co-signer accepted"]
    },
    {
        name: "Flexible Finance Corp",
        minCreditScore: "verypoor",
        minIncome: 20000,
        loanTypes: ["personal"],
        maxLoanAmount: 25000,
        employmentRequired: ["fulltime", "parttime"],
        approvalRate: 60,
        interestRate: "12.0% - 18.0%",
        features: ["No credit check options", "Quick approval", "Small loan specialist"]
    },
    {
        name: "HomeOwner's Bank",
        minCreditScore: "good",
        minIncome: 55000,
        loanTypes: ["home"],
        maxLoanAmount: 750000,
        employmentRequired: ["fulltime", "selfemployed", "retired"],
        approvalRate: 85,
        interestRate: "3.25% - 5.75%",
        features: ["Mortgage specialists", "First-time buyer programs", "Low down payment options"]
    }
];

// Credit score ranking for comparison
const creditScoreRank = {
    "excellent": 5,
    "good": 4,
    "fair": 3,
    "poor": 2,
    "verypoor": 1
};

// Match customer with banks
function matchBanks(customerData) {
    const matches = [];

    banks.forEach(bank => {
        let matchScore = 0;
        let reasons = [];

        // Check loan type
        if (!bank.loanTypes.includes(customerData.loanType)) {
            return; // Skip this bank
        }

        // Check credit score
        if (creditScoreRank[customerData.creditScore] < creditScoreRank[bank.minCreditScore]) {
            return; // Skip this bank
        } else if (creditScoreRank[customerData.creditScore] >= creditScoreRank[bank.minCreditScore]) {
            matchScore += 25;
            reasons.push("Credit score meets requirements");
        }

        // Check income
        if (customerData.income < bank.minIncome) {
            return; // Skip this bank
        } else {
            matchScore += 20;
            reasons.push("Income qualifies");
        }

        // Check loan amount
        if (customerData.loanAmount > bank.maxLoanAmount) {
            return; // Skip this bank
        } else {
            matchScore += 15;
            reasons.push("Loan amount within limits");
        }

        // Check employment
        if (!bank.employmentRequired.includes(customerData.employment)) {
            return; // Skip this bank
        } else {
            matchScore += 15;
            reasons.push("Employment status accepted");
        }

        // Bonus points for excellent credit
        if (customerData.creditScore === "excellent") {
            matchScore += 15;
        }

        // Bonus for income well above minimum
        if (customerData.income > bank.minIncome * 1.5) {
            matchScore += 10;
        }

        matches.push({
            bank: bank,
            matchScore: matchScore,
            reasons: reasons
        });
    });

    // Sort by match score (highest first)
    matches.sort((a, b) => b.matchScore - a.matchScore);

    return matches;
}

// Display results
function displayResults(matches) {
    const resultsContainer = document.getElementById('bankResults');
    resultsContainer.innerHTML = '';

    if (matches.length === 0) {
        resultsContainer.innerHTML = `
            <div class="no-results">
                <h3>No matches found</h3>
                <p>We couldn't find banks that match your current criteria. Consider:</p>
                <ul>
                    <li>Improving your credit score</li>
                    <li>Increasing your income</li>
                    <li>Reducing the loan amount</li>
                    <li>Working with a credit counselor</li>
                </ul>
            </div>
        `;
        return;
    }

    // Only show top 3 matches
    const topMatches = matches.slice(0, 3);

    topMatches.forEach((match, index) => {
        const bank = match.bank;
        const matchPercentage = Math.min(match.matchScore, 100);

        // Calculate approval likelihood based on match score and bank's base approval rate
        // Higher match score = higher likelihood relative to the bank's base rate
        const approvalLikelihood = Math.min(
            Math.round(bank.approvalRate * (matchPercentage / 100)),
            bank.approvalRate
        );

        let matchClass = 'high-match';
        if (matchPercentage < 70) matchClass = 'medium-match';
        if (matchPercentage < 50) matchClass = 'low-match';

        const bankCard = document.createElement('div');
        bankCard.className = `bank-card ${matchClass}`;
        bankCard.innerHTML = `
            <div class="bank-header">
                <h3>${index + 1}. ${bank.name}</h3>
                <div class="match-badge">
                    <span class="match-percentage">${matchPercentage}%</span>
                    <span class="match-label">Match</span>
                </div>
            </div>
            <div class="bank-info">
                <div class="info-row">
                    <span class="label">Approval Likelihood:</span>
                    <span class="value" style="color: #3ca6d8; font-weight: 700;">${approvalLikelihood}%</span>
                </div>
                <div class="info-row">
                    <span class="label">Interest Rate:</span>
                    <span class="value">${bank.interestRate}</span>
                </div>
                <div class="info-row">
                    <span class="label">Max Loan:</span>
                    <span class="value">$${bank.maxLoanAmount.toLocaleString()}</span>
                </div>
            </div>
            <div class="features">
                <h4>Key Features:</h4>
                <ul>
                    ${bank.features.map(feature => `<li>${feature}</li>`).join('')}
                </ul>
            </div>
            <div class="match-reasons">
                <h4>Why you match:</h4>
                <ul>
                    ${match.reasons.map(reason => `<li>${reason}</li>`).join('')}
                </ul>
            </div>
        `;
        resultsContainer.appendChild(bankCard);
    });
}

// Generate reference number
function generateReferenceNumber() {
    const timestamp = Date.now().toString(36).toUpperCase();
    const random = Math.random().toString(36).substring(2, 7).toUpperCase();
    return `AXP-${timestamp}-${random}`;
}

// Initialize EmailJS when page loads
window.addEventListener('load', function() {
    if (typeof emailjs !== 'undefined') {
        emailjs.init("VCRoHGxbB5ZkCxxUg");
        console.log('EmailJS initialized');
    } else {
        console.error('EmailJS failed to load');
    }
});

// Form submission - supports both match page (loanForm) and index page (leadForm)
document.addEventListener('DOMContentLoaded', function() {
    const loanForm = document.getElementById('loanForm');
    const leadForm = document.getElementById('leadForm');

    function handleApplicationSubmit(e, isLeadForm) {
        e.preventDefault();

        // Check if terms checkbox is checked
        const agreeToTerms = document.getElementById('agreeToTerms');
        if (!agreeToTerms) {
            alert('Form elements not found. Please refresh the page and try again.');
            console.error('agreeToTerms checkbox not found');
            return;
        }
        
        if (!agreeToTerms.checked) {
            alert('Please agree to the Privacy Policy and Terms and Conditions to continue.');
            agreeToTerms.focus();
            return;
        }

        // Check if EmailJS is loaded
        if (typeof emailjs === 'undefined') {
            alert('Email service is not available. Please refresh the page and try again.');
            console.error('EmailJS is not loaded');
            return;
        }

    // Collect customer data (for internal processing - not shown to customer)
    const customerData = {
        fullName: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        loanAmount: document.getElementById('loanAmount').value,
        businessName: document.getElementById('businessName').value,
        loanType: document.getElementById('loanType').value,
        creditScore: document.getElementById('creditScore').value,
        revenue: document.getElementById('revenue').value,
        yearsInBusiness: document.getElementById('yearsInBusiness').value,
        equipmentDescription: document.getElementById('equipmentDescription').value
    };

    // Generate reference number
    const referenceNumber = generateReferenceNumber();
    var refEl = document.getElementById('referenceNumber');
    var leadRefEl = document.getElementById('leadFormReference');
    if (refEl) refEl.textContent = referenceNumber;
    if (leadRefEl) leadRefEl.textContent = referenceNumber;

    // Show loading state
    const submitButton = e.target.querySelector('button[type="submit"]');
    const originalButtonText = submitButton.textContent;
    submitButton.textContent = 'Submitting...';
    submitButton.disabled = true;

    console.log('Sending application email with data:', customerData);

    // Check if we're on the co-branded page (rightmfgsystems.html)
    const isCobrandedPage = window.location.pathname.includes('rightmfgsystems.html');
    
    // Check for vendor email in URL parameters (for vendor partnerships)
    const urlParams = new URLSearchParams(window.location.search);
    const vendorEmail = urlParams.get('vendor');
    
    // Debug: log vendor email detection
    if (vendorEmail) {
        console.log('Vendor email detected:', vendorEmail);
    } else {
        console.log('No vendor email in URL');
    }
    
    // Prepare email template data
    const emailData = {
        full_name: customerData.fullName,
        email: customerData.email,
        phone: customerData.phone,
        loan_amount: customerData.loanAmount || 'Not specified',
        business_name: customerData.businessName || 'Not specified',
        loan_type: customerData.loanType,
        credit_score: customerData.creditScore,
        revenue: customerData.revenue || 'Not specified',
        years_in_business: customerData.yearsInBusiness || 'Not specified',
        equipment_description: customerData.equipmentDescription || 'N/A',
        reference_number: referenceNumber,
        to_email: 'alex@axiantpartners.com'
    };

    // If vendor email is provided in URL, send to both Axiant Partners and vendor
    if (vendorEmail) {
        // Decode URL-encoded email (in case of special characters)
        const decodedVendorEmail = decodeURIComponent(vendorEmail);
        
        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(decodedVendorEmail)) {
            console.error('Invalid vendor email format:', decodedVendorEmail);
            alert('Invalid vendor email in URL. Please contact support.');
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
            return;
        }
        
        console.log('Sending emails to Axiant Partners and vendor:', decodedVendorEmail);
        console.log('Full URL:', window.location.href);
        console.log('URL params:', window.location.search);
        
        // Add vendor email to email data so it's included in the email body
        const emailDataWithVendor = {
            ...emailData,
            vendor_email: decodedVendorEmail,
            vendor_note: `\n\n---\nThis application was submitted through a vendor partnership.\nVendor Email: ${decodedVendorEmail}\nPlease forward this application to the vendor.`
        };
        
        // Send to Axiant Partners (include vendor info in body)
        const email1 = emailjs.send('service_jweh7na', 'template_dmwg1ey', {
            ...emailDataWithVendor,
            to_email: 'alex@axiantpartners.com'
        }).then(function(response) {
            console.log('Email 1 (Axiant) sent successfully:', response);
            console.log('Response status:', response.status);
            console.log('Response text:', response.text);
            return response;
        }).catch(function(error) {
            console.error('Email 1 (Axiant) failed:', error);
            console.error('Error status:', error.status);
            console.error('Error text:', error.text);
            throw { email: 'Axiant', error: error };
        });
        
        // Send to vendor (using same template, different email)
        // Note: EmailJS may require vendor email to be whitelisted in service settings
        const email2 = emailjs.send('service_jweh7na', 'template_dmwg1ey', {
            ...emailData,
            to_email: decodedVendorEmail
        }).then(function(response) {
            console.log('Email 2 (Vendor) sent successfully:', response);
            console.log('Response status:', response.status);
            console.log('Response text:', response.text);
            return response;
        }).catch(function(error) {
            console.error('Email 2 (Vendor) failed:', error);
            console.error('Vendor email used:', decodedVendorEmail);
            console.error('Error status:', error.status);
            console.error('Error text:', error.text);
            console.error('Note: If this fails, the vendor email may need to be whitelisted in EmailJS service settings.');
            throw { email: 'Vendor', error: error };
        });
        
        // Send both emails in parallel
        Promise.allSettled([email1, email2])
        .then(function(results) {
            console.log('Email sending results:', results);
            
            const axiantResult = results[0];
            const vendorResult = results[1];
            
            // Check if Axiant email succeeded
            if (axiantResult.status === 'fulfilled') {
                console.log('Axiant email sent successfully');
            } else {
                console.error('Axiant email failed:', axiantResult.reason);
            }
            
            // Check if vendor email succeeded
            if (vendorResult.status === 'fulfilled') {
                console.log('Vendor email sent successfully');
            } else {
                console.error('Vendor email failed:', vendorResult.reason);
                console.error('This might be due to EmailJS template configuration. Make sure the template uses {{to_email}} variable.');
            }
            
            // Show success message even if one email fails (as long as Axiant email succeeds)
            if (axiantResult.status === 'fulfilled') {
                if (isLeadForm) {
                    var lf = document.getElementById('leadForm');
                    var lfTy = document.getElementById('leadFormThankYou');
                    if (lf) lf.style.display = 'none';
                    if (lf && lf.nextElementSibling) lf.nextElementSibling.style.display = 'none';
                    if (lfTy) lfTy.style.display = 'block';
                } else {
                    document.getElementById('applicationForm').style.display = 'none';
                    var ty = document.getElementById('thankYouContainer');
                    if (ty) ty.style.display = ty.classList.contains('match-thank-you') ? 'flex' : 'block';
                }
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                // Both emails failed or Axiant failed
                let errorMessage = 'Sorry, there was an error submitting your application. ';
                if (axiantResult.reason && axiantResult.reason.error && axiantResult.reason.error.status === 412) {
                    errorMessage += 'The email service connection needs to be updated. Please contact us directly at alex@axiantpartners.com or try again later.';
                } else {
                    errorMessage += 'Please contact us directly at alex@axiantpartners.com or try again later.';
                }
                
                alert(errorMessage);
                submitButton.textContent = originalButtonText;
                submitButton.disabled = false;
            }
        });
    }
    // If on co-branded page, send to both Axiant Partners and Right Manufacturing Systems
    else if (isCobrandedPage) {
        // Send to Axiant Partners
        const email1 = emailjs.send('service_jweh7na', 'template_dmwg1ey', {
            ...emailData,
            to_email: 'alex@axiantpartners.com'
        });
        
        // Send to Right Manufacturing Systems (using same template, different email)
        const email2 = emailjs.send('service_jweh7na', 'template_dmwg1ey', {
            ...emailData,
            to_email: 'ian@mixright.com'
        });
        
        // Send both emails in parallel
        Promise.all([email1, email2])
        .then(function(responses) {
            console.log('Both emails sent successfully!', responses);
            if (isLeadForm) {
                var lf = document.getElementById('leadForm');
                var lfTy = document.getElementById('leadFormThankYou');
                if (lf) lf.style.display = 'none';
                if (lf && lf.nextElementSibling) lf.nextElementSibling.style.display = 'none';
                if (lfTy) lfTy.style.display = 'block';
            } else {
                document.getElementById('applicationForm').style.display = 'none';
                var ty = document.getElementById('thankYouContainer');
                    if (ty) ty.style.display = ty.classList.contains('match-thank-you') ? 'flex' : 'block';
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        })
        .catch(function(error) {
            console.error('Email sending failed:', error);
            console.error('Error details:', JSON.stringify(error, null, 2));
            
            let errorMessage = 'Sorry, there was an error submitting your application. ';
            if (error.status === 412) {
                errorMessage += 'The email service connection needs to be updated. Please contact us directly at alex@axiantpartners.com or try again later.';
            } else {
                errorMessage += 'Please contact us directly at alex@axiantpartners.com or try again later.';
            }
            
            alert(errorMessage);
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        });
    } else {
        // Regular page - send to both Axiant Partners addresses
        var email1 = emailjs.send('service_jweh7na', 'template_dmwg1ey', { ...emailData, to_email: 'alex@axiantpartners.com' });
        var email2 = emailjs.send('service_jweh7na', 'template_dmwg1ey', { ...emailData, to_email: 'jerry@axiantpartners.com' });
        Promise.allSettled([email1, email2])
        .then(function(results) {
            var axiantOk = results[0].status === 'fulfilled';
            if (axiantOk) {
                console.log('Application email sent successfully!');
                if (isLeadForm) {
                    var lf = document.getElementById('leadForm');
                    var lfTy = document.getElementById('leadFormThankYou');
                    if (lf) lf.style.display = 'none';
                    if (lf && lf.nextElementSibling) lf.nextElementSibling.style.display = 'none';
                    if (lfTy) lfTy.style.display = 'block';
                } else {
                    document.getElementById('applicationForm').style.display = 'none';
                    var ty = document.getElementById('thankYouContainer');
                    if (ty) ty.style.display = ty.classList.contains('match-thank-you') ? 'flex' : 'block';
                }
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                console.error('Email sending failed:', results[0].reason);
                var err = results[0].reason && results[0].reason.error ? results[0].reason.error : {};
                var errorMessage = 'Sorry, there was an error submitting your application. ';
                errorMessage += (err.status === 412) ? 'The email service connection needs to be updated. ' : '';
                errorMessage += 'Please contact us directly at alex@axiantpartners.com or try again later.';
                alert(errorMessage);
                submitButton.textContent = originalButtonText;
                submitButton.disabled = false;
            }
        });
    }
    }

    if (loanForm) {
        loanForm.addEventListener('submit', function(e) { handleApplicationSubmit(e, false); });
    }
    if (leadForm) {
        leadForm.addEventListener('submit', function(e) { handleApplicationSubmit(e, true); });
    }

    // New application button
    const newApplicationBtn = document.getElementById('newApplication');
    if (newApplicationBtn) {
        newApplicationBtn.addEventListener('click', function() {
            const applicationForm = document.getElementById('applicationForm');
            const thankYouContainer = document.getElementById('thankYouContainer');
            const loanForm = document.getElementById('loanForm');
            
            if (applicationForm) applicationForm.style.display = 'block';
            if (thankYouContainer) thankYouContainer.style.display = 'none';
            if (loanForm) loanForm.reset();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
