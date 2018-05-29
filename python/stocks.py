import os
import csv
import json
import yaml
import plotly.plotly as py
import plotly.tools as pt
import plotly.graph_objs as go
import pandas_datareader.data as web

from datetime import datetime
from datetime import timedelta
from iexfinance import Stock

csv_path = "build/readme/example.csv"
def data(tickers, sector):
    slist = []
    print(tickers)
    stocks_object = Stock(tickers)
    stocks = stocks_object.get_price()
    now = datetime.now()
    last_year = datetime.now() - timedelta(days=365)
    date = datetime.today().strftime('%Y-%m-%d')
    for company in stocks:
        # Create one-year graph trend for company
        df = web.DataReader(company, 'robinhood', datetime(last_year.year, last_year.month, last_year.day), datetime(now.year, now.month, now.day)).reset_index()
        data = [go.Scatter(x=df.begins_at, y=df.close_price)]
        layout = go.Layout(title=company, xaxis={'title': 'Date'}, yaxis={'title':'Close Price'})
        figure = go.Figure(data=data, layout=layout)
        link = py.plot(figure, filename=company)

        # Get closing price of company
        price = stocks[company]

        # Link to company graph
        company_graph = "[{}]({})".format(company, link)

        # Output company info
        slist.append([date, company_graph, price])
    output(slist)

def setup():
    # Set plotly credentials
    pt.set_credentials_file(username='ogoyal', api_key=os.environ['API_KEY'])

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
