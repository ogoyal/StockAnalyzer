# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.89 | 
| 2017-08-21| ATVI| 61.73 | 
| 2017-08-21| MSFT| 72.05 | 
| 2017-08-21| GE| 24.48 | 
| 2017-08-21| BA| 234.91 | 
| 2017-08-21| AMD| 11.93 | 
| 2017-08-21| BOX| 18.84 | 
| 2017-08-21| FB| 167.55 | 
| 2017-08-21| AMZN| 951.38 | 
| 2017-08-21| PCG| 69.30 | 
| 2017-08-21| AAPL| 157.10 | 
| 2017-08-21| AMC| 12.68 | 
| 2017-08-21| P| 8.09 | 
| 2017-08-21| WMT| 79.99 | 
| 2017-08-21| FDX| 206.25 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

