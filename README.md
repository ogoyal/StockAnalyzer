# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 159.15 | 
| 2017-08-17| ATVI| 61.94 | 
| 2017-08-17| MSFT| 72.80 | 
| 2017-08-17| GE| 24.95 | 
| 2017-08-17| BA| 235.85 | 
| 2017-08-17| AMD| 12.47 | 
| 2017-08-17| BOX| 18.76 | 
| 2017-08-17| FB| 168.15 | 
| 2017-08-17| AMZN| 964.93 | 
| 2017-08-17| PCG| 69.25 | 
| 2017-08-17| AAPL| 158.73 | 
| 2017-08-17| AMC| 13.52 | 
| 2017-08-17| P| 8.51 | 
| 2017-08-17| WMT| 79.20 | 
| 2017-08-17| FDX| 206.32 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

