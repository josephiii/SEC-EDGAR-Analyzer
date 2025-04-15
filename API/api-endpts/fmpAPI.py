
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
    
    def incomeStatement(self):
        pass

    def balanceSheet(self):
        pass

    def cashFlow(self):
        pass