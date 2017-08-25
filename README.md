# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.68 | 
| 2017-08-25| ATVI| 62.63 | 
| 2017-08-25| MSFT| 72.91 | 
| 2017-08-25| GE| 24.58 | 
| 2017-08-25| BA| 236.52 | 
| 2017-08-25| AMD| 12.45 | 
| 2017-08-25| BOX| 19.64 | 
| 2017-08-25| FB| 166.88 | 
| 2017-08-25| AMZN| 948.12 | 
| 2017-08-25| PCG| 70.18 | 
| 2017-08-25| AAPL| 160.08 | 
| 2017-08-25| AMC| 13.02 | 
| 2017-08-25| P| 8.15 | 
| 2017-08-25| WMT| 78.85 | 
| 2017-08-25| FDX| 208.53 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

