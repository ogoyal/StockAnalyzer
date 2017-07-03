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
    def __init__(self, slist=[], name=''):
        self.slist = slist
        if self.slist != []:
            self.name = slist[0]
            self.company = Share(self.name)
        if name != "":
            self.name = name

    def __iter__(self):
        for company in self.slist:
            scalc = Stock(company)
            scalc_date = scalc.get_date()
            scalc_price = scalc.get_price()
            scalc_delta = scalc.get_delta()
            yield [scalc_date, company, scalc_price, scalc_delta]

    def get_price(self):
        return self.company.get_price()

    def get_date(self):
        try:
            full_date = self.company.get_trade_datetime()
            self.date = full_date.split(' ')[0]
        except:
            self.date = "---"
        return self.date

    def get_delta(self):
        return self.company.get_change()

def output(slist):
    f = open('example.csv', 'wt')
    company = Stock(slist)
    cline = company.__iter__()
    try:
        writer = csv.writer(f)
        writer.writerow(('Date', 'Stocks', 'Price($)', 'Change($)'))
        for i in range(len(slist)):
            writer.writerow(cline.next())
    finally:
        f.close()

def main():
    tickers = []
    f = open('tickers.txt', 'r')
    for line in f:
        tickers.append(line.strip())
    f.close()
    output(tickers)
 

if __name__== "__main__":
    main()

