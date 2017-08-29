# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 152.06 | 
| 2017-08-29| ATVI| 62.80 | 
| 2017-08-29| MSFT| 72.51 | 
| 2017-08-29| GE| 24.33 | 
| 2017-08-29| BA| 237.47 | 
| 2017-08-29| AMD| 11.99 | 
| 2017-08-29| BOX| 19.23 | 
| 2017-08-29| FB| 166.66 | 
| 2017-08-29| AMZN| 943.00 | 
| 2017-08-29| PCG| 70.30 | 
| 2017-08-29| AAPL| 161.40 | 
| 2017-08-29| AMC| 12.70 | 
| 2017-08-29| P| 8.03 | 
| 2017-08-29| WMT| 78.39 | 
| 2017-08-29| FDX| 207.82 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

