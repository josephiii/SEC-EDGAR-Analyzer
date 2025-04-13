document.addEventListener("DOMContentLoaded", function(){

    const form = document.getElementById('edgar-form');

    form.addEventListener('submit', function(event){
        event.preventDefault();

        const tickerInput = document.getElementById('ticker');
        const ticker = tickerInput.value.trim().toUpperCase();

        if(!ticker){
            alert("Please enter a ticker symbol!");
            return;
        }

        fetchTickerData(ticker);
    });
});

function fetchTickerData(ticker){

    //optional add loding indicator

    fetch(`/api/ticker/${ticker}`)
    .then(response => {
        if(response.ok){
            return response.json();
        } else{
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
    })
    .then(data => {
        displayTickerData(data);
    })
    .catch(error => {
        alert('Error fetching data: ' + error.message);
        
    });
}

function displayTickerData(data){

    document.getElementById('company-name').textContent = data.name;
    document.getElementById('company-symbol').textContent = data.symbol;

    //add website code

    // may need to format these for larger numbers
    document.getElementById('price').textContent = data.price
    doucment.getElementById('shares').textContent = data.shares
    document.getElementById('marketCap').textContent = data.marketCap;
    document.getElementById('totalCash').textContent = data.totalCash;
    document.getElementById('totalDebt').textContent = data.totalDebt;
    document.getElementById('enterpriseValue').textContent = data.enterpriseValue;
    
    document.getElementById('company-sector').textContent = data.sector;
    document.getElementById('company-industry').textContent = data.industry;
}









// grab ticker from form

// display general data for ticker
/*

- company name
- current price
- market cap
- company size listing
- sector/ industry
- enterprise val
- biggest competetors
- largest shareholders
- dividend yield
- etc.

Financial Statment look up---
- specify form type 8-k, 10-k, 10-q
- date (year, quarter)
*/