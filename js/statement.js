document.addEventListener('DOMContentLoaded', function(){
    
    const period = document.getElementById('period');
    const year = document.getElementById('year');
    const ticker = localStorage.getItem('ticker');

    createYears();

    loadData(ticker, period.value, year.value);

    period.addEventListener('change', function(){
        loadData(ticker, period.value, year.value);
    })

    year.addEventListener('change', function(){
        loadData(ticker, period.value, year.value);
    })
    
});

async function loadData(ticker, period, year){

    try{
        const [incomeData, balanceData, cashFlowData] = await Promise.all([
            getIncomeStatement(ticker, period, year),
            getBalanceSheet(ticker, period, year),
            getCashFlowStatement(ticker, period, year)
        ]);

        displayIncomeStatement(incomeData);
        displayBalanceSheet(balanceData);
        displayCashFlowStatement(cashFlowData);

    } catch(error){
        console.log(`Issue loading financial statements: ${error}`);
        alert(`Failed to load data: ${error.message}`);
    }
}

function displayIncomeStatement(data){
    if(!data || data.length === 0){ 
        alert('No Income Statement data is avalable at this time');
        return
    }

    document.getElementById('revenue').textContent = data.revenue;
    document.getElementById('cor').textContent = data.costOfRevenue;
    document.getElementById('gross-profit').textContent = data.grossProfit;
    document.getElementById('operating-expenses').textContent = data.operatingExpenses;
    document.getElementById('operating-income').textContent = data.operatingIncome;
    document.getElementById('net-income').textContent = data.netIncome;
    document.getElementById('eps').textContent = data.eps;

}

function displayBalanceSheet(data){
    if(!data || data.length === 0){ 
        alert('No Balance Sheet data is avalable at this time');
        return
    }

    document.getElementById('total-assets').textContent = data.totalAssets;
    document.getElementById('total-liabilities').textContent = data.totalLiabilities;
    document.getElementById('cash').textContent = data.cashAndCashEquivalents;
    document.getElementById('debt').textContent = data.totalDebt;
    document.getElementById('total-equity').textContent = data.totalEquity;

}

function displayCashFlowStatement(data){
    if(!data || data.length === 0){ 
        alert('No Balance Sheet data is avalable at this time');
        return
    }

    document.getElementById('cf-net-income').textContent = data.netIncome;
    document.getElementById('net-cash').textContent = data.netChangeInCash;
    document.getElementById('capital-expenditure').textContent = data.capitalExpenditure;
    document.getElementById('debt-repayment').textContent = data.debtRepayment;
    document.getElementById('free-cash-flow').textContent = data.freeCashFlow;

}
    

async function getIncomeStatement(ticker, period, year){
    const response = await fetch(`/api/income-statement/${ticker}?period=${period}&year=${year}`);

    if(!response.ok){
        throw new Error(`Error fetching Income Statement: ${response.statusText}`);
    } 
    return response.json();
}

async function getBalanceSheet(ticker, period, year){
    const response = await fetch(`/api/balance-sheet/${ticker}?period=${period}&year=${year}`);

    if(!response.ok){
        throw new Error(`Error fetching Balance Sheet: ${response.statusText}`);
    }
    return response.json();
}

async function getCashFlowStatement(ticker, period, year){
    const response = await fetch(`/api/cash-flow-statement/${ticker}?period=${period}&year=${year}`);

    if(!response.ok){
        throw new Error(`Error fetching Cash Flow Statement: ${response.statusText}`)
    }
    return response.json();
}
    
    

function createYears(){
    
    const yearSelect = document.getElementById('year');
    const currentYear = new Date().getFullYear();

    yearSelect.innerHTML = '';

    for (let year = 2000; year <= currentYear; year++) {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearSelect.appendChild(option);
    }
}