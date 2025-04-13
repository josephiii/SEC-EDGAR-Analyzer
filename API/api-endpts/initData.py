
from fastapi import FastAPI, HTTPException
import uvicorn
import yfinance as yf

app = FastAPI()

@app.get('/api/ticker/{ticker}')
def tickerData(ticker: str):
     
    try:
        stock = yf.Ticker(ticker)
        stockInfo = stock.info

        response = {
            'name': stockInfo.get('shortName', 'N/A'),
            'symbol': stockInfo.get('symbol', 'N/A'),
            'website': stockInfo.get('website', 'N/A'),

            'price': stockInfo.get('currentPrice', stockInfo.get('regularMarketPrice', 'N/A')),
            'shares': stockInfo.get('sharesOutstanding', 'N/A'),
            'marketCap': stockInfo.get('marketCap', 'N/A'),
            'totalCash': stockInfo.get('totalCash', 'N/A'),
            'totalDebt': stockInfo.get('totalDebt', 'N/A'),
            'enterpriseValue': stockInfo.get('enterpriseValue', 'N/A'),

            'sector': stockInfo.get('sector', 'N/A'),
            'industry': stockInfo.get('industry', 'N/A')
        }
        return response
    
    except Exception as error:
        raise HTTPException(status_code=404, detail=f"Error fetching {ticker} data: {error}")
            

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="5500" )