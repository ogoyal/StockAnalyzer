# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-11| COST| 156.65 | 
| 2017-08-11| ATVI| 60.74 | 
| 2017-08-11| MSFT| 72.50 | 
| 2017-08-11| GE| 25.20 | 
| 2017-08-11| BA| 234.88 | 
| 2017-08-11| AMD| 12.23 | 
| 2017-08-11| BOX| 18.23 | 
| 2017-08-11| FB| 168.08 | 
| 2017-08-11| AMZN| 967.99 | 
| 2017-08-11| PCG| 69.02 | 
| 2017-08-11| AAPL| 157.48 | 
| 2017-08-11| AMC| 14.05 | 
| 2017-08-11| P| 8.08 | 
| 2017-08-11| WMT| 80.40 | 
| 2017-08-11| FDX| 204.87 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

