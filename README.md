# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-23| COST| 159.37 | 
| 2017-08-23| ATVI| 64.01 | 
| 2017-08-23| MSFT| 72.72 | 
| 2017-08-23| GE| 24.39 | 
| 2017-08-23| BA| 238.09 | 
| 2017-08-23| AMD| 12.48 | 
| 2017-08-23| BOX| 19.53 | 
| 2017-08-23| FB| 168.71 | 
| 2017-08-23| AMZN| 958.00 | 
| 2017-08-23| PCG| 69.90 | 
| 2017-08-23| AAPL| 159.98 | 
| 2017-08-23| AMC| 12.55 | 
| 2017-08-23| P| 8.35 | 
| 2017-08-23| WMT| 79.96 | 
| 2017-08-23| FDX| 207.07 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

