# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.22 | 
| 2017-08-29| ATVI| 63.31 | 
| 2017-08-29| MSFT| 72.95 | 
| 2017-08-29| GE| 24.42 | 
| 2017-08-29| BA| 239.11 | 
| 2017-08-29| AMD| 12.02 | 
| 2017-08-29| BOX| 19.42 | 
| 2017-08-29| FB| 168.19 | 
| 2017-08-29| AMZN| 953.76 | 
| 2017-08-29| PCG| 70.27 | 
| 2017-08-29| AAPL| 162.38 | 
| 2017-08-29| AMC| 12.68 | 
| 2017-08-29| P| 8.04 | 
| 2017-08-29| WMT| 78.60 | 
| 2017-08-29| FDX| 210.57 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

