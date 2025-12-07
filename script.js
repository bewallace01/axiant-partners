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

// Form submission
document.getElementById('loanForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Check if terms checkbox is checked
    const agreeToTerms = document.getElementById('agreeToTerms');
    if (!agreeToTerms.checked) {
        alert('Please agree to the Privacy Policy and Terms and Conditions to continue.');
        agreeToTerms.focus();
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
        yearsInBusiness: parseFloat(document.getElementById('yearsInBusiness').value),
        equipmentDescription: document.getElementById('equipmentDescription').value
    };

    // In a real implementation, this would send data to your server
    // For now, we'll just log it to console
    console.log('Application submitted:', customerData);

    // Generate reference number
    const referenceNumber = generateReferenceNumber();
    document.getElementById('referenceNumber').textContent = referenceNumber;

    // Hide form, show thank you message
    document.getElementById('applicationForm').style.display = 'none';
    document.getElementById('thankYouContainer').style.display = 'block';

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// New application button
document.getElementById('newApplication').addEventListener('click', function() {
    document.getElementById('applicationForm').style.display = 'block';
    document.getElementById('thankYouContainer').style.display = 'none';
    document.getElementById('loanForm').reset();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
