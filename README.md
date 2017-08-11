# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-11| COST| 156.92 | 
| 2017-08-11| ATVI| 60.65 | 
| 2017-08-11| MSFT| 71.84 | 
| 2017-08-11| GE| 25.28 | 
| 2017-08-11| BA| 233.59 | 
| 2017-08-11| AMD| 12.08 | 
| 2017-08-11| BOX| 18.36 | 
| 2017-08-11| FB| 167.59 | 
| 2017-08-11| AMZN| 965.80 | 
| 2017-08-11| PCG| 69.29 | 
| 2017-08-11| AAPL| 157.22 | 
| 2017-08-11| AMC| 13.90 | 
| 2017-08-11| P| 7.99 | 
| 2017-08-11| WMT| 80.62 | 
| 2017-08-11| FDX| 205.65 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

