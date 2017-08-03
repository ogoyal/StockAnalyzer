#import sys
#sys.path.append("..")
#import python.stocks
import unittest
from yahoo_finance import Share

class StockAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.company = Share("GOOG")
    
    '''
    Test Yahoo Api Functions
    '''
    def test_get_price(self):
        price = self.company.get_price()
        self.assertTrue(price)
    
    def test_get_change(self):
        change_in_currency = self.company.get_change()
        self.assertTrue(change_in_currency)

    def test_get_percent_change(self):
        change_in_percent = self.company.get_percent_change()
        self.assertTrue(change_in_percent)

    def test_get_trade_datetime(self):
        date = self.company.get_trade_datetime()
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

