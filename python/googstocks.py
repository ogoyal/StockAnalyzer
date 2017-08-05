import os
import csv
import json
from googlefinance import getQuotes

'''
{u'Index': u'NASDAQ', u'LastTradeWithCurrency': u'927.96', u'LastTradeDateTime': u'2017-08-04T16:00:00Z', u'LastTradePrice': u'927.96', u'LastTradeTime': u'4:00PM EDT', u'LastTradeDateTimeLong': u'Aug 4, 4:00PM EDT', u'StockSymbol': u'GOOG', u'ID': u'304466804484872'}
'''

def data(tickers):
    slist = []
    stocks = getQuotes(tickers)
    for stock in stocks:
        json_string = json.dumps(stock)
        parsed_json = json.loads(json_string)
        date = parsed_json['LastTradeDateTime'].split('T')[0]
        symbol = parsed_json['StockSymbol']
        price = parsed_json['LastTradePrice']
        slist.append([date, symbol, price])
    output(slist)
        
def output(slist):
    f = open('example.csv', 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(('Date', 'Stocks', 'Price($)'))
        for data in slist:
            writer.writerow(data)
    finally:
        f.close()

def main():
    
    tickers = []
    if os.path.isfile('tickers.txt'):
        f = open('tickers.txt', 'r')
        for line in f:
            tickers.append(line.strip())
        f.close()
    data(tickers)

if __name__== "__main__":
    main()

