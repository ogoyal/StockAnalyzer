from django.shortcuts import render
from yahoo_finance import Share
# Create your views here.

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

def rank_list(request):
    tickers = []
    fopen = open('../tickers.txt', 'r')
    for line in fopen:
        tickers.append(line.strip())
    fopen.close()

    #company = Stock(tickers)

    return render(request, 'template/rank_list.html', {'tickers': tickers})



