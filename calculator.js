/**
 * Business Loan & Lease Calculator
 * Toggle: Loan vs Lease. Loan uses Purchase Price - Down Payment. Lease uses Purchase Price - Down Payment - Residual.
 * Calculates payment, amount financed, interest rate, or term when 3 of 4 are provided.
 */
(function () {
    'use strict';

    const PAYMENTS_PER_YEAR = {
        monthly: 12,
        quarterly: 4,
        biannually: 2,
        annually: 1
    };

    function parseNumber(val, allowEmpty) {
        if (val == null) return allowEmpty ? null : NaN;
        const s = String(val).trim();
        if (s === '') return allowEmpty ? null : NaN;
        const cleaned = s.replace(/[$,%\s]/g, '');
        const n = parseFloat(cleaned);
        return isNaN(n) ? (allowEmpty ? null : NaN) : n;
    }

    function isLeaseMode() {
        return document.getElementById('modeLease')?.classList.contains('active');
    }

    function getInputs() {
        const mode = isLeaseMode();
        const purchasePrice = parseNumber(document.getElementById('purchasePrice')?.value, true);
        const downPayment = parseNumber(document.getElementById('downPayment')?.value, true) ?? 0;
        const residualValue = mode ? (parseNumber(document.getElementById('residualValue')?.value, true) ?? 0) : 0;
        const paymentAmount = parseNumber(document.getElementById('paymentAmount')?.value, true);
        const interestRate = parseNumber(document.getElementById('interestRate')?.value, true);
        const loanTerm = parseNumber(document.getElementById('loanTerm')?.value, true);
        const termUnit = document.getElementById('termUnit')?.value || 'months';
        const paymentFreq = document.getElementById('paymentFrequency')?.value || 'monthly';

        const ppy = PAYMENTS_PER_YEAR[paymentFreq] || 12;
        const termMonths = loanTerm != null ? (termUnit === 'years' ? loanTerm * 12 : loanTerm) : null;
        const numPayments = termMonths != null ? Math.round((termMonths / 12) * ppy) : null;

        // Amount financed: Loan = Price - Down; Lease = Price - Down - Residual
        let loanAmount = null;
        if (purchasePrice != null && purchasePrice > 0) {
            const pv = purchasePrice - downPayment - residualValue;
            loanAmount = pv > 0 ? pv : null;
        }

        return {
            purchasePrice, downPayment, residualValue,
            loanAmount, paymentAmount, interestRate, loanTerm,
            termUnit, paymentFreq, ppy, numPayments, mode
        };
    }

    function calcPaymentWithFreq(PV, annualRate, numPayments, ppy) {
        if (PV <= 0 || numPayments <= 0) return null;
        const r = (annualRate / 100) / ppy;
        if (r <= 0) return PV / numPayments;
        return (r * PV) / (1 - Math.pow(1 + r, -numPayments));
    }

    function calcLoanAmount(P, annualRate, numPayments, ppy) {
        if (P <= 0 || numPayments <= 0) return null;
        const r = (annualRate / 100) / ppy;
        if (r <= 0) return P * numPayments;
        return P * (1 - Math.pow(1 + r, -numPayments)) / r;
    }

    function calcNumPayments(PV, P, annualRate, ppy) {
        if (PV <= 0 || P <= 0) return null;
        const r = (annualRate / 100) / ppy;
        if (r <= 0) return Math.ceil(PV / P);
        const ratio = (r * PV) / P;
        if (ratio >= 1) return null;
        return Math.ceil(-Math.log(1 - ratio) / Math.log(1 + r));
    }

    function calcRate(PV, P, numPayments, ppy) {
        if (PV <= 0 || P <= 0 || numPayments <= 0) return null;
        const targetP = P;
        let lo = 0.0001;
        let hi = 100;
        for (let i = 0; i < 100; i++) {
            const mid = (lo + hi) / 2;
            const p = calcPaymentWithFreq(PV, mid, numPayments, ppy);
            if (p == null || p >= targetP) hi = mid;
            else lo = mid;
        }
        const finalP = calcPaymentWithFreq(PV, lo, numPayments, ppy);
        return Math.abs((finalP || 0) - targetP) < 0.01 ? lo : null;
    }

    function formatCurrency(n) {
        if (n == null || isNaN(n)) return '-';
        return '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function formatPercent(n) {
        if (n == null || isNaN(n)) return '-';
        return n.toFixed(2) + '%';
    }

    function formatTerm(numPayments, ppy, termUnit) {
        if (numPayments == null) return '-';
        const months = (numPayments / ppy) * 12;
        if (termUnit === 'years') return Math.round(months / 12) + ' years';
        return Math.round(months) + ' months';
    }

    function formatFreq(key) {
        const labels = { monthly: 'Monthly', quarterly: 'Quarterly', biannually: 'Bi-Annually', annually: 'Annually' };
        return labels[key] || key;
    }

    function showError(msg) {
        alert(msg);
    }

    function runCalculation() {
        const { purchasePrice, downPayment, residualValue, loanAmount, paymentAmount, interestRate, loanTerm, termUnit, paymentFreq, ppy, numPayments, mode } = getInputs();

        const filled = [loanAmount != null || purchasePrice != null, paymentAmount != null, interestRate != null, numPayments != null].filter(Boolean).length;
        if (filled < 3) {
            showError('Please fill in at least 3 of: Purchase Price, Payment Amount, Interest Rate, and Loan Term.');
            return;
        }

        let PV = loanAmount;
        let P = paymentAmount;
        let r = interestRate;
        let n = numPayments;
        let PP = purchasePrice;

        if (PV != null && PV <= 0) { showError('Amount financed must be positive. Check Purchase Price, Down Payment, and Residual.'); return; }
        if (P != null && P <= 0) { showError('Payment Amount must be positive.'); return; }
        if (r != null && (r < 0 || r > 100)) { showError('Interest Rate must be between 0 and 100.'); return; }
        if (n != null && n <= 0) { showError('Loan Term must be positive.'); return; }

        const res = residualValue ?? 0;
        const down = downPayment ?? 0;

        if (PV == null) {
            PV = calcLoanAmount(P, r, n, ppy);
            if (PV == null) { showError('Cannot calculate Amount Financed with the given inputs.'); return; }
            PP = PV + down + res;
        }
        if (P == null) {
            P = calcPaymentWithFreq(PV, r, n, ppy);
            if (P == null) { showError('Cannot calculate Payment Amount with the given inputs.'); return; }
        }
        if (r == null) {
            r = calcRate(PV, P, n, ppy);
            if (r == null) { showError('Cannot calculate Interest Rate with the given inputs.'); return; }
        }
        if (n == null) {
            n = calcNumPayments(PV, P, r, ppy);
            if (n == null) { showError('Cannot calculate Loan Term with the given inputs.'); return; }
        }
        if (PP == null) {
            PP = PV + down + res;
        }

        const totalPaid = P * n;
        const totalInterest = totalPaid - PV;
        const resultTermMonths = (n / ppy) * 12;

        document.getElementById('resultPurchasePrice').textContent = formatCurrency(PP);
        document.getElementById('resultDownPayment').textContent = formatCurrency(down);
        document.getElementById('resultLoanAmount').textContent = formatCurrency(PV);
        if (mode) {
            document.getElementById('resultRowResidual').style.display = '';
            document.getElementById('resultResidual').textContent = formatCurrency(res);
        } else {
            document.getElementById('resultRowResidual').style.display = 'none';
        }
        document.getElementById('resultPaymentAmount').textContent = formatCurrency(P) + ' per ' + formatFreq(paymentFreq).toLowerCase().replace('-annually', '-annually');
        document.getElementById('resultInterestRate').textContent = formatPercent(r);
        document.getElementById('resultLoanTerm').textContent = (termUnit === 'years' ? Math.round(resultTermMonths / 12) + ' years' : Math.round(resultTermMonths) + ' months');
        document.getElementById('resultPaymentFrequency').textContent = formatFreq(paymentFreq);
        document.getElementById('resultTotalPaid').textContent = formatCurrency(totalPaid);
        document.getElementById('resultTotalInterest').textContent = formatCurrency(totalInterest);

        openResultsModal();
    }

    function setMode(mode) {
        const isLease = mode === 'lease';
        document.getElementById('modeLoan').classList.toggle('active', !isLease);
        document.getElementById('modeLease').classList.toggle('active', isLease);
        document.getElementById('modeLoan').setAttribute('aria-pressed', !isLease);
        document.getElementById('modeLease').setAttribute('aria-pressed', isLease);
        const introLoan = document.querySelector('.calc-intro-loan');
        const introLease = document.querySelector('.calc-intro-lease');
        if (introLoan) introLoan.style.display = isLease ? 'none' : '';
        if (introLease) introLease.style.display = isLease ? '' : 'none';
        const residualField = document.querySelector('.calc-field-residual');
        if (residualField) residualField.style.display = isLease ? '' : 'none';
        const resInput = document.getElementById('residualValue');
        if (resInput && !isLease) resInput.value = '';
    }

    function closeResultsModal() {
        const results = document.getElementById('calculatorResults');
        if (results) {
            results.style.display = 'none';
            results.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }

    function openResultsModal() {
        const results = document.getElementById('calculatorResults');
        if (results) {
            results.style.display = 'flex';
            results.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
        }
    }

    function resetForm() {
        const form = document.getElementById('calculatorForm');
        if (form) form.reset();
        const down = document.getElementById('downPayment');
        if (down) down.value = '';
        const res = document.getElementById('residualValue');
        if (res) res.value = '';
        closeResultsModal();
    }

    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('calculatorForm');
        const clearBtn = document.getElementById('clearForm');
        const newCalcBtn = document.getElementById('newCalculation');
        const modeLoan = document.getElementById('modeLoan');
        const modeLease = document.getElementById('modeLease');

        if (modeLoan) modeLoan.addEventListener('click', function () { setMode('loan'); });
        if (modeLease) modeLease.addEventListener('click', function () { setMode('lease'); });
        if (form) form.addEventListener('submit', function (e) { e.preventDefault(); runCalculation(); });
        if (clearBtn) clearBtn.addEventListener('click', resetForm);
        if (newCalcBtn) newCalcBtn.addEventListener('click', resetForm);
        const backdrop = document.getElementById('calcModalBackdrop');
        if (backdrop) backdrop.addEventListener('click', closeResultsModal);
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                const res = document.getElementById('calculatorResults');
                if (res && res.style.display === 'flex') closeResultsModal();
            }
        });
    });
})();
