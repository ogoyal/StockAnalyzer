# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.24 | 
| 2017-09-01| ATVI| 65.12 | 
| 2017-09-01| MSFT| 73.94 | 
| 2017-09-01| GE| 25.14 | 
| 2017-09-01| BA| 240.33 | 
| 2017-09-01| AMD| 13.19 | 
| 2017-09-01| BOX| 19.06 | 
| 2017-09-01| FB| 172.02 | 
| 2017-09-01| AMZN| 978.25 | 
| 2017-09-01| PCG| 69.87 | 
| 2017-09-01| AAPL| 164.05 | 
| 2017-09-01| AMC| 14.15 | 
| 2017-09-01| P| 8.31 | 
| 2017-09-01| WMT| 78.37 | 
| 2017-09-01| FDX| 215.05 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

