# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.30 | 
| 2017-08-29| ATVI| 63.53 | 
| 2017-08-29| MSFT| 72.96 | 
| 2017-08-29| GE| 24.41 | 
| 2017-08-29| BA| 240.10 | 
| 2017-08-29| AMD| 12.07 | 
| 2017-08-29| BOX| 19.32 | 
| 2017-08-29| FB| 167.78 | 
| 2017-08-29| AMZN| 953.02 | 
| 2017-08-29| PCG| 70.22 | 
| 2017-08-29| AAPL| 162.40 | 
| 2017-08-29| AMC| 12.52 | 
| 2017-08-29| P| 8.07 | 
| 2017-08-29| WMT| 78.68 | 
| 2017-08-29| FDX| 210.49 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

