# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 158.77 | 
| 2017-08-17| ATVI| 61.83 | 
| 2017-08-17| MSFT| 72.72 | 
| 2017-08-17| GE| 24.90 | 
| 2017-08-17| BA| 235.74 | 
| 2017-08-17| AMD| 12.45 | 
| 2017-08-17| BOX| 18.72 | 
| 2017-08-17| FB| 168.06 | 
| 2017-08-17| AMZN| 965.02 | 
| 2017-08-17| PCG| 69.24 | 
| 2017-08-17| AAPL| 158.77 | 
| 2017-08-17| AMC| 13.35 | 
| 2017-08-17| P| 8.51 | 
| 2017-08-17| WMT| 79.28 | 
| 2017-08-17| FDX| 205.86 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

