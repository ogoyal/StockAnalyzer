# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.59 | 
| 2017-08-25| ATVI| 62.58 | 
| 2017-08-25| MSFT| 72.88 | 
| 2017-08-25| GE| 24.57 | 
| 2017-08-25| BA| 236.68 | 
| 2017-08-25| AMD| 12.42 | 
| 2017-08-25| BOX| 19.59 | 
| 2017-08-25| FB| 166.52 | 
| 2017-08-25| AMZN| 948.53 | 
| 2017-08-25| PCG| 70.17 | 
| 2017-08-25| AAPL| 160.23 | 
| 2017-08-25| AMC| 13.12 | 
| 2017-08-25| P| 8.11 | 
| 2017-08-25| WMT| 78.79 | 
| 2017-08-25| FDX| 208.70 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

