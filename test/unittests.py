import json
import yaml
import unittest
import datetime
from iexfinance import Stock
#from googlefinance import getQuotes (DEPRECATED)

class StockAnalyzerTest(unittest.TestCase):

    def setUp(self):
        stock = Stock("GOOG")
        self.company = stock.get_price()
        # stock = getQuotes("GOOG")[0]  (DEPRECATED)
        # json_string = json.dumps(stock)
        # parsed_json = json.loads(json_string)


    '''
    Test Google Api Functions
    '''
    def test_get_date(self):
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.assertTrue(date)

    def test_symbol(self):
        symbol = self.company.keys()
        self.assertTrue(symbol)

    def test_get_price(self):
        price = self.company['GOOG']
        self.assertTrue(price)

    '''
    Test tickers.yml
    '''
    def test_tickers(self):
        with open('tickers.yml', 'r') as stream:
            tickers = yaml.load(stream)
	self.assertTrue(tickers)
