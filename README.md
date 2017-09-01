# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.16 | 
| 2017-09-01| ATVI| 65.09 | 
| 2017-09-01| MSFT| 74.04 | 
| 2017-09-01| GE| 25.23 | 
| 2017-09-01| BA| 241.08 | 
| 2017-09-01| AMD| 13.13 | 
| 2017-09-01| BOX| 19.06 | 
| 2017-09-01| FB| 172.25 | 
| 2017-09-01| AMZN| 979.67 | 
| 2017-09-01| PCG| 69.89 | 
| 2017-09-01| AAPL| 164.10 | 
| 2017-09-01| AMC| 14.23 | 
| 2017-09-01| P| 8.31 | 
| 2017-09-01| WMT| 78.42 | 
| 2017-09-01| FDX| 215.78 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

