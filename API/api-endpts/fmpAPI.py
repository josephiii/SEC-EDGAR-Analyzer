
import requests

class fmpAPI:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseUrl = "https://financialmodelingprep.com/api/v3/"

    def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        
        params['apikey'] = self.apiKey
        url = f"{self.baseUrl}/{endpoint}"

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def incomeStatement(self, symbol, period="annual", limit=5, datatype="json", year=None, quarter=None):
        
        endpoint = f"income-statement/{symbol}"
        params = {
            'period': period,
            'limit': limit,
            'datatype': datatype
        }

        if year != None:
            params['year'] = year
        if quarter != None and period == 'quarter':
            params['quarter'] = quarter

        return self._request(endpoint, params)

    def balanceSheet(self, symbol, period="annual", limit=5, datatype="json", year=None, quarter=None):
        
        endpoint = f"balance-sheet-statement/{symbol}"
        params = {
            'period': period,
            'limit': limit,
            'datatype': datatype
        }

        if year != None:
            params['year'] = year
        if quarter != None and period == 'quarter':
            params['quarter'] = quarter

        return self._request(endpoint, params)

    def cashFlow(self, symbol, period="annual", limit=5, datatype="json", year=None, quarter=None):
        
        endpoint = f"cash-flow-statement/{symbol}"
        params = {
            'period': period,
            'limit': limit,
            'datatype': datatype
        }

        if year != None:
            params['year'] = year
        if quarter != None and period == 'quarter':
            params['quarter'] = quarter

        return self._request(endpoint, params)