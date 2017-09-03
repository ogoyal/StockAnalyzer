import json
import yaml
import unittest
from googlefinance import getQuotes

class StockAnalyzerTest(unittest.TestCase):

    def setUp(self):
        stock = getQuotes("GOOG")[0]
        json_string = json.dumps(stock)
        parsed_json = json.loads(json_string)
	self.company = parsed_json
    
    '''
    Test Google Api Functions
    '''
    def test_get_date(self):
        price = self.company['LastTradeDateTime'].split('T')[0]
        self.assertTrue(price)

    def test_symbol(self):
        symbol = self.company['StockSymbol']
        self.assertTrue(symbol)

    def test_get_price(self):
        date = self.company['LastTradePrice']
        self.assertTrue(date)

    '''
    Test tickers.yml
    '''
    def test_tickers(self):
        with open('tickers.yml', 'r') as stream:
            tickers = yaml.load(stream)
	self.assertTrue(tickers)

