# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-15| COST| 157.74 | 
| 2017-08-15| ATVI| 61.61 | 
| 2017-08-15| MSFT| 73.25 | 
| 2017-08-15| GE| 25.16 | 
| 2017-08-15| BA| 238.19 | 
| 2017-08-15| AMD| 12.87 | 
| 2017-08-15| BOX| 18.61 | 
| 2017-08-15| FB| 170.60 | 
| 2017-08-15| AMZN| 983.36 | 
| 2017-08-15| PCG| 69.36 | 
| 2017-08-15| AAPL| 161.37 | 
| 2017-08-15| AMC| 12.95 | 
| 2017-08-15| P| 8.33 | 
| 2017-08-15| WMT| 81.25 | 
| 2017-08-15| FDX| 209.32 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

