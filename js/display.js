document.addEventListener("DOMContentLoaded", function (event) {
    event.preventDefault();
    const ticker = localStorage.getItem('ticker')

    if (!ticker) {
        alert("No ticker symbol found in URL.");
        window.location.href="/";
        return;
    }

    fetchTickerData(ticker);
});


function fetchTickerData(ticker){
    //optional add loading indicator

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

    if(data.website && data.website !== 'N/A'){
        const webLink = document.createElement('a');
        webLink.href = data.website;
        webLink.textContent = data.website;
        webLink.target = "_blank";

        document.getElementById('company-website').textContent = '';
        document.getElementById('company-website').appendChild(webLink);
    } else {
        document.getElementById('website').textContent = data.name + 'does not have an official website';
    }

    // may need to format these for larger numbers
    document.getElementById('price').textContent = data.price
    document.getElementById('shares').textContent = data.shares
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