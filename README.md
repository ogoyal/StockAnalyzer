# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 158.73 | 
| 2017-08-17| ATVI| 61.45 | 
| 2017-08-17| MSFT| 72.50 | 
| 2017-08-17| GE| 24.75 | 
| 2017-08-17| BA| 235.75 | 
| 2017-08-17| AMD| 12.35 | 
| 2017-08-17| BOX| 18.60 | 
| 2017-08-17| FB| 166.99 | 
| 2017-08-17| AMZN| 961.20 | 
| 2017-08-17| PCG| 69.07 | 
| 2017-08-17| AAPL| 157.96 | 
| 2017-08-17| AMC| 13.20 | 
| 2017-08-17| P| 8.48 | 
| 2017-08-17| WMT| 79.60 | 
| 2017-08-17| FDX| 205.58 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

