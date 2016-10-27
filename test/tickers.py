from yahoo_finance import Share

def rank_list():
    tickers = {}
    fopen = open('tickers.txt', 'r')
    for line in fopen:
        key = line.strip()
        price = get_price(key)
        tickers[key] = price
    fopen.close()
    return tickers

def get_price(name):
    company = Share(name)
    return company.get_price()

def main():
    output = rank_list()
    print output
main()
