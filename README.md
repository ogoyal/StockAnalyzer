# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.18 | 
| 2017-09-01| ATVI| 64.76 | 
| 2017-09-01| MSFT| 73.75 | 
| 2017-09-01| GE| 25.17 | 
| 2017-09-01| BA| 241.13 | 
| 2017-09-01| AMD| 13.23 | 
| 2017-09-01| BOX| 19.25 | 
| 2017-09-01| FB| 172.55 | 
| 2017-09-01| AMZN| 979.81 | 
| 2017-09-01| PCG| 69.82 | 
| 2017-09-01| AAPL| 164.02 | 
| 2017-09-01| AMC| 14.02 | 
| 2017-09-01| P| 8.44 | 
| 2017-09-01| WMT| 78.34 | 
| 2017-09-01| FDX| 215.97 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

