# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.66 | 
| 2017-08-21| ATVI| 61.72 | 
| 2017-08-21| MSFT| 72.00 | 
| 2017-08-21| GE| 24.48 | 
| 2017-08-21| BA| 234.85 | 
| 2017-08-21| AMD| 11.94 | 
| 2017-08-21| BOX| 18.86 | 
| 2017-08-21| FB| 167.54 | 
| 2017-08-21| AMZN| 951.17 | 
| 2017-08-21| PCG| 69.31 | 
| 2017-08-21| AAPL| 156.76 | 
| 2017-08-21| AMC| 12.77 | 
| 2017-08-21| P| 8.06 | 
| 2017-08-21| WMT| 79.98 | 
| 2017-08-21| FDX| 206.28 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

