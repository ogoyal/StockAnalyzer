import os
import csv
import json
import yaml
import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web

from datetime import datetime
from iexfinance import Stock

csv_path = "build/readme/example.csv"
def data(tickers, sector):
    slist = []
    print(tickers)
    stocks_object = Stock(tickers)
    stocks = stocks_object.get_price()
    date = datetime.today().strftime('%Y-%m-%d')
    for company in stocks:
        price = stocks[company]
        slist.append([date, company, price])
    output(slist)

def setup():
    if os.path.isfile(csv_path):
        os.remove(csv_path)
    f = open(csv_path, 'a+')
    try:
        writer = csv.writer(f)
        writer.writerow(('Date', 'Stocks', 'Price($)'))
    finally:
        f.close()

def output(slist):
    f = open(csv_path, 'a+')
    try:
        writer = csv.writer(f)
        for data in slist:
            writer.writerow(data)
    finally:
        f.close()

def main():
    setup()
    if os.path.isfile('tickers.yml'):
        with open("tickers.yml", 'r') as stream:
            try:
                tickers = yaml.load(stream)
                sectors = tickers["sectors"]
                for key in sorted(sectors, key=len):
                    data(sectors[key], key)
            except yaml.YAMLError as exc:
                print(exc)

if __name__== "__main__":
    main()
