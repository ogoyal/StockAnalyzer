# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 158.76 | 
| 2017-08-17| ATVI| 61.66 | 
| 2017-08-17| MSFT| 72.69 | 
| 2017-08-17| GE| 24.86 | 
| 2017-08-17| BA| 236.17 | 
| 2017-08-17| AMD| 12.42 | 
| 2017-08-17| BOX| 18.70 | 
| 2017-08-17| FB| 167.79 | 
| 2017-08-17| AMZN| 964.36 | 
| 2017-08-17| PCG| 69.16 | 
| 2017-08-17| AAPL| 158.62 | 
| 2017-08-17| AMC| 13.55 | 
| 2017-08-17| P| 8.51 | 
| 2017-08-17| WMT| 79.43 | 
| 2017-08-17| FDX| 206.11 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

