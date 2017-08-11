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
| 2017-08-11| ATVI| 60.92 | 
| 2017-08-11| MSFT| 72.34 | 
| 2017-08-11| GE| 25.30 | 
| 2017-08-11| BA| 234.68 | 
| 2017-08-11| AMD| 12.25 | 
| 2017-08-11| BOX| 18.48 | 
| 2017-08-11| FB| 168.24 | 
| 2017-08-11| AMZN| 968.74 | 
| 2017-08-11| PCG| 69.22 | 
| 2017-08-11| AAPL| 157.84 | 
| 2017-08-11| AMC| 14.10 | 
| 2017-08-11| P| 8.06 | 
| 2017-08-11| WMT| 80.67 | 
| 2017-08-11| FDX| 205.99 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

