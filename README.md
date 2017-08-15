# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-15| COST| 157.43 | 
| 2017-08-15| ATVI| 61.62 | 
| 2017-08-15| MSFT| 73.17 | 
| 2017-08-15| GE| 25.15 | 
| 2017-08-15| BA| 238.65 | 
| 2017-08-15| AMD| 12.98 | 
| 2017-08-15| BOX| 18.64 | 
| 2017-08-15| FB| 171.28 | 
| 2017-08-15| AMZN| 985.66 | 
| 2017-08-15| PCG| 69.40 | 
| 2017-08-15| AAPL| 161.59 | 
| 2017-08-15| AMC| 13.25 | 
| 2017-08-15| P| 8.36 | 
| 2017-08-15| WMT| 81.24 | 
| 2017-08-15| FDX| 209.59 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

