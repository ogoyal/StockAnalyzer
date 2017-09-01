# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.38 | 
| 2017-09-01| ATVI| 64.93 | 
| 2017-09-01| MSFT| 73.96 | 
| 2017-09-01| GE| 25.18 | 
| 2017-09-01| BA| 241.51 | 
| 2017-09-01| AMD| 13.16 | 
| 2017-09-01| BOX| 19.17 | 
| 2017-09-01| FB| 172.25 | 
| 2017-09-01| AMZN| 980.09 | 
| 2017-09-01| PCG| 69.88 | 
| 2017-09-01| AAPL| 163.92 | 
| 2017-09-01| AMC| 14.23 | 
| 2017-09-01| P| 8.36 | 
| 2017-09-01| WMT| 78.39 | 
| 2017-09-01| FDX| 216.05 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

