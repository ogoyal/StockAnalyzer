# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.61 | 
| 2017-08-21| ATVI| 61.76 | 
| 2017-08-21| MSFT| 72.11 | 
| 2017-08-21| GE| 24.58 | 
| 2017-08-21| BA| 235.15 | 
| 2017-08-21| AMD| 11.96 | 
| 2017-08-21| BOX| 18.81 | 
| 2017-08-21| FB| 167.11 | 
| 2017-08-21| AMZN| 950.60 | 
| 2017-08-21| PCG| 69.24 | 
| 2017-08-21| AAPL| 156.46 | 
| 2017-08-21| AMC| 12.68 | 
| 2017-08-21| P| 8.14 | 
| 2017-08-21| WMT| 79.59 | 
| 2017-08-21| FDX| 205.84 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

