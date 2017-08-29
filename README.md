# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.33 | 
| 2017-08-29| ATVI| 63.33 | 
| 2017-08-29| MSFT| 72.89 | 
| 2017-08-29| GE| 24.41 | 
| 2017-08-29| BA| 239.12 | 
| 2017-08-29| AMD| 12.02 | 
| 2017-08-29| BOX| 19.34 | 
| 2017-08-29| FB| 167.82 | 
| 2017-08-29| AMZN| 952.26 | 
| 2017-08-29| PCG| 70.21 | 
| 2017-08-29| AAPL| 162.23 | 
| 2017-08-29| AMC| 12.73 | 
| 2017-08-29| P| 8.05 | 
| 2017-08-29| WMT| 78.60 | 
| 2017-08-29| FDX| 210.22 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

