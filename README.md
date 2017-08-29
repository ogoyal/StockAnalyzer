# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.14 | 
| 2017-08-29| ATVI| 63.18 | 
| 2017-08-29| MSFT| 72.88 | 
| 2017-08-29| GE| 24.37 | 
| 2017-08-29| BA| 238.97 | 
| 2017-08-29| AMD| 12.00 | 
| 2017-08-29| BOX| 19.32 | 
| 2017-08-29| FB| 167.70 | 
| 2017-08-29| AMZN| 950.95 | 
| 2017-08-29| PCG| 70.18 | 
| 2017-08-29| AAPL| 162.71 | 
| 2017-08-29| AMC| 12.65 | 
| 2017-08-29| P| 8.08 | 
| 2017-08-29| WMT| 78.46 | 
| 2017-08-29| FDX| 210.42 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

