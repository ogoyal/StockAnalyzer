# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-14| COST| 157.91 | 
| 2017-08-14| ATVI| 61.89 | 
| 2017-08-14| MSFT| 73.59 | 
| 2017-08-14| GE| 25.36 | 
| 2017-08-14| BA| 237.15 | 
| 2017-08-14| AMD| 12.76 | 
| 2017-08-14| BOX| 18.53 | 
| 2017-08-14| FB| 170.75 | 
| 2017-08-14| AMZN| 983.30 | 
| 2017-08-14| PCG| 69.17 | 
| 2017-08-14| AAPL| 159.85 | 
| 2017-08-14| AMC| 13.60 | 
| 2017-08-14| P| 8.07 | 
| 2017-08-14| WMT| 80.70 | 
| 2017-08-14| FDX| 207.86 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

