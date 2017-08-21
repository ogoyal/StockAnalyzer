# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.07 | 
| 2017-08-21| ATVI| 61.78 | 
| 2017-08-21| MSFT| 72.15 | 
| 2017-08-21| GE| 24.49 | 
| 2017-08-21| BA| 235.68 | 
| 2017-08-21| AMD| 12.05 | 
| 2017-08-21| BOX| 18.91 | 
| 2017-08-21| FB| 167.78 | 
| 2017-08-21| AMZN| 953.29 | 
| 2017-08-21| PCG| 69.35 | 
| 2017-08-21| AAPL| 157.21 | 
| 2017-08-21| AMC| 13.05 | 
| 2017-08-21| P| 8.10 | 
| 2017-08-21| WMT| 79.71 | 
| 2017-08-21| FDX| 206.33 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

