# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.58 | 
| 2017-08-29| ATVI| 63.56 | 
| 2017-08-29| MSFT| 73.09 | 
| 2017-08-29| GE| 24.44 | 
| 2017-08-29| BA| 240.71 | 
| 2017-08-29| AMD| 12.15 | 
| 2017-08-29| BOX| 19.30 | 
| 2017-08-29| FB| 168.04 | 
| 2017-08-29| AMZN| 953.77 | 
| 2017-08-29| PCG| 70.21 | 
| 2017-08-29| AAPL| 163.02 | 
| 2017-08-29| AMC| 12.82 | 
| 2017-08-29| P| 8.10 | 
| 2017-08-29| WMT| 78.86 | 
| 2017-08-29| FDX| 211.22 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

