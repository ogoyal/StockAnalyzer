# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.71 | 
| 2017-08-25| ATVI| 62.76 | 
| 2017-08-25| MSFT| 72.78 | 
| 2017-08-25| GE| 24.58 | 
| 2017-08-25| BA| 236.46 | 
| 2017-08-25| AMD| 12.36 | 
| 2017-08-25| BOX| 19.68 | 
| 2017-08-25| FB| 166.57 | 
| 2017-08-25| AMZN| 948.12 | 
| 2017-08-25| PCG| 70.27 | 
| 2017-08-25| AAPL| 160.01 | 
| 2017-08-25| AMC| 13.15 | 
| 2017-08-25| P| 8.16 | 
| 2017-08-25| WMT| 78.80 | 
| 2017-08-25| FDX| 208.81 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

