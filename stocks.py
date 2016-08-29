import csv
from yahoo_finance import Share

class Stock(object):
    def __init__(self, name):
        self.name = name
        self.company = Share(self.name)
        self.get_price()
        self.get_date()

    def get_price(self):
        self.price = self.company.get_price()

    def get_date(self):
        self.date = self.company.get_trade_datetime()

    def show_price(self):
        print("{}: {}".format(self.name, self.price))
	return self.price

def output(slist):
    f = open('stocks.csv', 'wt')
    lines = favorite(slist)
    try:
        writer = csv.writer(f)
        writer.writerow(('Date', 'Stocks', 'Price'))
        for i in range(0, len(lines)):
            writer.writerow(lines[i])
    finally:
        f.close()

def myList():
    slist = ['COST','ATVI','MSFT','GE','BA']
    output(slist)

def favorite(slist):
    lines = []
    for i in range(0,len(slist)):
        stock = Stock(slist[i])
        line = [stock.date, stock.name, stock.price]
	lines.append(line)
    return lines

def interactive():
    slist = []
    while(1):
        company = raw_input("Enter stock name: ")
        stock = Stock(company)
        exist = stock.show_price()
	if exist:
	  ok = raw_input("Do you want to add to favorites?(y/n): ")
	  if ok == 'y':
            slist.append(stock.name)
	  else:
	    pass
	try:
          cont = input("Enter 0 to quit, 1 to continue: ")
          if not cont:
	      output(slist)
              break
        except:
          print "Error"

def main():
    myList()

if __name__== "__main__":
    main()

