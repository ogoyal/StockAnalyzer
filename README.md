# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-26| COST| 151.92| -1.25| -0.82% | 
| 2017-07-25| ATVI| 60.95| -0.49| -0.80% | 
| 2017-07-25| MSFT| 74.19| +0.59| +0.80% | 
| 2017-07-25| GE| 25.44| +0.01| +0.04% | 
| 2017-07-25| BA| 212.46| +0.28| +0.13% | 
| 2017-07-25| AMD| 14.11| -0.05| -0.35% | 
| 2017-07-25| BOX| 19.89| +0.20| +1.02% | 
| 2017-07-25| FB| 165.28| -0.72| -0.43% | 
| 2017-07-25| AMZN| 1039.87| +0.92| +0.09% | 
| 2017-07-25| PCG| 67.51| -0.39| -0.57% | 
| 2017-07-25| AAPL| 152.74| +0.65| +0.43% | 
| 2017-07-25| AMC| 20.85| +0.35| +1.71% | 
| 2017-07-25| P| 9.83| +0.19| +1.97% | 
| 2017-07-25| WMT| 78.52| +1.63| +2.12% | 
| 2017-07-25| FDX| 214.37| +1.69| +0.79% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

