# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-15| COST| 157.32 | 
| 2017-08-15| ATVI| 61.79 | 
| 2017-08-15| MSFT| 73.29 | 
| 2017-08-15| GE| 25.11 | 
| 2017-08-15| BA| 237.39 | 
| 2017-08-15| AMD| 12.90 | 
| 2017-08-15| BOX| 18.64 | 
| 2017-08-15| FB| 170.84 | 
| 2017-08-15| AMZN| 985.10 | 
| 2017-08-15| PCG| 69.37 | 
| 2017-08-15| AAPL| 161.19 | 
| 2017-08-15| AMC| 13.20 | 
| 2017-08-15| P| 8.40 | 
| 2017-08-15| WMT| 80.84 | 
| 2017-08-15| FDX| 209.43 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

