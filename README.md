# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 158.93 | 
| 2017-08-17| ATVI| 62.14 | 
| 2017-08-17| MSFT| 72.97 | 
| 2017-08-17| GE| 24.95 | 
| 2017-08-17| BA| 236.14 | 
| 2017-08-17| AMD| 12.52 | 
| 2017-08-17| BOX| 18.79 | 
| 2017-08-17| FB| 168.48 | 
| 2017-08-17| AMZN| 965.20 | 
| 2017-08-17| PCG| 69.22 | 
| 2017-08-17| AAPL| 158.99 | 
| 2017-08-17| AMC| 13.40 | 
| 2017-08-17| P| 8.52 | 
| 2017-08-17| WMT| 79.04 | 
| 2017-08-17| FDX| 206.41 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

