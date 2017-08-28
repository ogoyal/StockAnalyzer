# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.13 | 
| 2017-08-28| ATVI| 62.49 | 
| 2017-08-28| MSFT| 72.72 | 
| 2017-08-28| GE| 24.42 | 
| 2017-08-28| BA| 236.82 | 
| 2017-08-28| AMD| 12.17 | 
| 2017-08-28| BOX| 19.69 | 
| 2017-08-28| FB| 166.74 | 
| 2017-08-28| AMZN| 946.05 | 
| 2017-08-28| PCG| 69.97 | 
| 2017-08-28| AAPL| 161.01 | 
| 2017-08-28| AMC| 13.07 | 
| 2017-08-28| P| 8.14 | 
| 2017-08-28| WMT| 78.03 | 
| 2017-08-28| FDX| 208.32 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

