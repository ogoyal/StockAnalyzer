# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.42 | 
| 2017-08-21| ATVI| 61.53 | 
| 2017-08-21| MSFT| 71.88 | 
| 2017-08-21| GE| 24.49 | 
| 2017-08-21| BA| 234.72 | 
| 2017-08-21| AMD| 11.93 | 
| 2017-08-21| BOX| 18.77 | 
| 2017-08-21| FB| 166.87 | 
| 2017-08-21| AMZN| 950.49 | 
| 2017-08-21| PCG| 69.25 | 
| 2017-08-21| AAPL| 155.95 | 
| 2017-08-21| AMC| 12.52 | 
| 2017-08-21| P| 8.13 | 
| 2017-08-21| WMT| 79.50 | 
| 2017-08-21| FDX| 205.58 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

