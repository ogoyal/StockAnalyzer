#
#  stocks.py
#  Programming in Python
#
#  Created by Ojas Goyal on 7/30/16.
#  Copyright (c) 2016 Ojas Goyal. All rights reserved.
#

import csv
from yahoo_finance import Share

class Stock(object):
    def __init__(self, name):
        self.name = name
        self.company = Share(self.name)
        self.get_price()
        self.get_date()
        self.get_delta()

    def get_price(self):
        self.price = self.company.get_price()

    def get_date(self):
        full_date = self.company.get_trade_datetime()
        self.date = full_date.split(' ')[0]

    def get_delta(self):
        self.delta = self.company.get_change()

def output(slist):
    f = open('example.csv', 'wt')
    lines = data(slist)
    try:
        writer = csv.writer(f)
        writer.writerow(('Date', 'Stocks', 'Price($)', 'Change($)'))
        for i in range(0, len(lines)):
            writer.writerow(lines[i])
    finally:
        f.close()

def data(slist):
    lines = []
    for i in range(0,len(slist)):
        stock = Stock(slist[i])
        line = [stock.date, stock.name, stock.price, stock.delta]
	lines.append(line)
    return lines

def main():
    tickers = []
    f = open('tickers.txt', 'r')
    for line in f:
        tickers.append(line.strip())
    f.close()
    output(tickers)

if __name__== "__main__":
    main()

