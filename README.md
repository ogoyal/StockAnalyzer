# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 152.54 | 
| 2017-08-29| ATVI| 63.10 | 
| 2017-08-29| MSFT| 72.74 | 
| 2017-08-29| GE| 24.33 | 
| 2017-08-29| BA| 237.74 | 
| 2017-08-29| AMD| 12.05 | 
| 2017-08-29| BOX| 19.31 | 
| 2017-08-29| FB| 167.60 | 
| 2017-08-29| AMZN| 948.91 | 
| 2017-08-29| PCG| 70.29 | 
| 2017-08-29| AAPL| 162.35 | 
| 2017-08-29| AMC| 12.80 | 
| 2017-08-29| P| 8.10 | 
| 2017-08-29| WMT| 78.78 | 
| 2017-08-29| FDX| 209.07 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

