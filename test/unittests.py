import json
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
    Test tickers.txt
    '''
    def test_tickers(self):
        tickers = []
        f = open('tickers.txt', 'r')
        for line in f:
	    tickers.append(line.strip())
        f.close()
	self.assertTrue(tickers)

