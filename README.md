# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 152.88 | 
| 2017-08-29| ATVI| 63.13 | 
| 2017-08-29| MSFT| 72.84 | 
| 2017-08-29| GE| 24.33 | 
| 2017-08-29| BA| 238.65 | 
| 2017-08-29| AMD| 12.06 | 
| 2017-08-29| BOX| 19.34 | 
| 2017-08-29| FB| 167.74 | 
| 2017-08-29| AMZN| 953.00 | 
| 2017-08-29| PCG| 70.29 | 
| 2017-08-29| AAPL| 162.77 | 
| 2017-08-29| AMC| 12.60 | 
| 2017-08-29| P| 8.10 | 
| 2017-08-29| WMT| 78.51 | 
| 2017-08-29| FDX| 209.25 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

