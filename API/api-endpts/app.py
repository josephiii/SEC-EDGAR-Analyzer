
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import yfinance as yf
import os

app = FastAPI()

#I dont understand the path handling but it works
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
app.mount('/static', StaticFiles(directory=os.path.join(ROOT, 'static')), name='static')
app.mount('/js', StaticFiles(directory=os.path.join(ROOT, 'js')), name='js')


@app.get('/')
def index():
    return FileResponse(os.path.join(ROOT, 'templates', 'index.html'))

@app.get('/display')
def display():
    return FileResponse(os.path.join(ROOT, 'templates', 'display.html'))

@app.get('/statement')
def statement():
    return FileResponse(os.path.join(ROOT, 'templates', 'statement.html'))


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
    uvicorn.run(app, host="127.0.0.1", port=8000)