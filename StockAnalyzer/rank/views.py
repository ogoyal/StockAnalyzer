from django.shortcuts import render
from yahoo_finance import Share
# Create your views here.

def rank_list(request):
    tickers = []
    fopen = open('../tickers.txt', 'r')
    for line in fopen:
        tickers.append(line.strip())
    fopen.close()

    return render(request, 'template/rank_list.html', {'tickers': tickers})

