# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.89 | 
| 2017-08-29| ATVI| 63.64 | 
| 2017-08-29| MSFT| 73.14 | 
| 2017-08-29| GE| 24.44 | 
| 2017-08-29| BA| 240.91 | 
| 2017-08-29| AMD| 12.16 | 
| 2017-08-29| BOX| 19.43 | 
| 2017-08-29| FB| 168.25 | 
| 2017-08-29| AMZN| 954.48 | 
| 2017-08-29| PCG| 70.29 | 
| 2017-08-29| AAPL| 162.87 | 
| 2017-08-29| AMC| 12.70 | 
| 2017-08-29| P| 8.10 | 
| 2017-08-29| WMT| 78.92 | 
| 2017-08-29| FDX| 211.48 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

