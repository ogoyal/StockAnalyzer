# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.56 | 
| 2017-08-29| ATVI| 63.48 | 
| 2017-08-29| MSFT| 73.05 | 
| 2017-08-29| GE| 24.44 | 
| 2017-08-29| BA| 240.49 | 
| 2017-08-29| AMD| 12.15 | 
| 2017-08-29| BOX| 19.28 | 
| 2017-08-29| FB| 168.05 | 
| 2017-08-29| AMZN| 954.06 | 
| 2017-08-29| PCG| 70.26 | 
| 2017-08-29| AAPL| 162.91 | 
| 2017-08-29| AMC| 12.85 | 
| 2017-08-29| P| 8.11 | 
| 2017-08-29| WMT| 78.77 | 
| 2017-08-29| FDX| 211.30 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

