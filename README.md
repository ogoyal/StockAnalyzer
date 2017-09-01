# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.09 | 
| 2017-09-01| ATVI| 64.86 | 
| 2017-09-01| MSFT| 73.79 | 
| 2017-09-01| GE| 25.13 | 
| 2017-09-01| BA| 241.36 | 
| 2017-09-01| AMD| 13.31 | 
| 2017-09-01| BOX| 19.24 | 
| 2017-09-01| FB| 172.47 | 
| 2017-09-01| AMZN| 980.62 | 
| 2017-09-01| PCG| 69.82 | 
| 2017-09-01| AAPL| 164.16 | 
| 2017-09-01| AMC| 13.95 | 
| 2017-09-01| P| 8.44 | 
| 2017-09-01| WMT| 78.39 | 
| 2017-09-01| FDX| 216.11 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

