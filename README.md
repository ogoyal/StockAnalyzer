# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-11| COST| 157.09 | 
| 2017-08-11| ATVI| 60.58 | 
| 2017-08-11| MSFT| 71.74 | 
| 2017-08-11| GE| 25.29 | 
| 2017-08-11| BA| 233.11 | 
| 2017-08-11| AMD| 12.33 | 
| 2017-08-11| BOX| 18.24 | 
| 2017-08-11| FB| 168.28 | 
| 2017-08-11| AMZN| 962.16 | 
| 2017-08-11| PCG| 69.27 | 
| 2017-08-11| AAPL| 158.01 | 
| 2017-08-11| AMC| 14.25 | 
| 2017-08-11| P| 8.13 | 
| 2017-08-11| WMT| 80.75 | 
| 2017-08-11| FDX| 205.36 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

