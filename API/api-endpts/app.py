
from fastapi import FastAPI, HTTPException, Query
from fmpAPI import fmpAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional
import uvicorn
import yfinance as yf
import os
import apiConfig


app = FastAPI()
fmpClient = fmpAPI(apiConfig.fmpAPIKEY)

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
    
@app.get('/api/income-statement/{ticker}')
def getIncomeStatement(
    ticker: str,
    period: Optional[str] = Query('annual', enum=['annual', 'quarter-one', 'quarter-two', 'quarter-three', 'quarter-four']),
    limit: Optional[int] = Query(5, ge=1, le=5),
    year: Optional[int] = None,
    quarter: Optional[int] = Query(None, ge=1, le=4)
):
    try:

        if period != 'annual':
            if period == 'quarter-one':
                quarter = 1
            elif period == 'quarter-two':
                quarter = 2
            elif period == 'quarter-three':
                quarter = 3
            elif period == 'quarter-four':
                quarter = 4
            
            period = 'quarter'

        data = fmpClient.incomeStatement(symbol=ticker, period=period, limit=limit, year=year, quarter=quarter)

        if not data:
            raise HTTPException(status_code=404, detail=f"No Income Statement data for {ticker}")
        return data
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error fetching Income Statement for {ticker}: {error}")

@app.get('/api/balance-sheet/{ticker}')
def getBalanceSheet(
    ticker: str,
    period: Optional[str] = Query('annual', enum=['annual', 'quarter-one', 'quarter-two', 'quarter-three', 'quarter-four']),
    limit: Optional[int] = Query(5, ge=1, le=5),
    year: Optional[int] = None,
    quarter: Optional[int] = Query(None, ge=1, le=4)
):
    try:
        
        if period != 'annual':
            if period == 'quarter-one':
                quarter = 1
            elif period == 'quarter-two':
                quarter = 2
            elif period == 'quarter-three':
                quarter = 3
            elif period == 'quarter-four':
                quarter = 4
            
            period = 'quarter'

        data = fmpClient.balanceSheet(symbol=ticker, period=period, limit=limit, year=year, quarter=quarter)

        if not data:
            raise HTTPException(status_code=404, detail=f"No Balance Sheet data for {ticker}")
        return data
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error fetching Balance Sheet for {ticker}: {error}")
    
@app.get('/api/cash-flow-statement/{ticker}')
def getCashFlow(
    ticker: str,
    period: Optional[str] = Query('annual', enum=['annual', 'quarter-one', 'quarter-two', 'quarter-three', 'quarter-four']),
    limit: Optional[int] = Query(5, ge=1, le=5),
    year: Optional[int] = None,
    quarter: Optional[int] = Query(None, ge=1, le=4)
):
    try:

        if period != 'annual':
            if period == 'quarter-one':
                quarter = 1
            elif period == 'quarter-two':
                quarter = 2
            elif period == 'quarter-three':
                quarter = 3
            elif period == 'quarter-four':
                quarter = 4
            
            period = 'quarter'

        data = fmpClient.cashFlow(symbol=ticker, period=period, limit=limit, year=year, quarter=quarter)

        if not data:
            raise HTTPException(status_code=404, detail=f"No Cash Flow Statement for {ticker}")
        return data
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error fetching Cash Flow Statment for {ticker}: {error}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)