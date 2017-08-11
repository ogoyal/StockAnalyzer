# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-11| COST| 157.18 | 
| 2017-08-11| ATVI| 60.59 | 
| 2017-08-11| MSFT| 72.04 | 
| 2017-08-11| GE| 25.31 | 
| 2017-08-11| BA| 233.86 | 
| 2017-08-11| AMD| 12.12 | 
| 2017-08-11| BOX| 18.34 | 
| 2017-08-11| FB| 167.97 | 
| 2017-08-11| AMZN| 968.35 | 
| 2017-08-11| PCG| 69.36 | 
| 2017-08-11| AAPL| 157.77 | 
| 2017-08-11| AMC| 13.98 | 
| 2017-08-11| P| 8.01 | 
| 2017-08-11| WMT| 80.73 | 
| 2017-08-11| FDX| 205.82 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

