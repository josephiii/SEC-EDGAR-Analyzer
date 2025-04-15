document.addEventListener("DOMContentLoaded", function(){
    const form = document.getElementById('edgar-form');

    form.addEventListener('submit', function(event){
        const tickerInput = document.getElementById('ticker');
        const ticker = tickerInput.value.trim().toUpperCase();

        if(!ticker){
            alert('Please Enter a Valid Symbol!');
            event.preventDefault();
            return;
        }

        localStorage.setItem('ticker', ticker);
        
    });
});