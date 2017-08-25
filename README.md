# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.26 | 
| 2017-08-25| ATVI| 62.65 | 
| 2017-08-25| MSFT| 72.64 | 
| 2017-08-25| GE| 24.50 | 
| 2017-08-25| BA| 236.77 | 
| 2017-08-25| AMD| 12.31 | 
| 2017-08-25| BOX| 19.73 | 
| 2017-08-25| FB| 166.64 | 
| 2017-08-25| AMZN| 948.83 | 
| 2017-08-25| PCG| 70.24 | 
| 2017-08-25| AAPL| 159.43 | 
| 2017-08-25| AMC| 13.15 | 
| 2017-08-25| P| 8.22 | 
| 2017-08-25| WMT| 78.80 | 
| 2017-08-25| FDX| 208.21 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

