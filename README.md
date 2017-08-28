# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 151.91 | 
| 2017-08-28| ATVI| 62.60 | 
| 2017-08-28| MSFT| 72.70 | 
| 2017-08-28| GE| 24.41 | 
| 2017-08-28| BA| 237.45 | 
| 2017-08-28| AMD| 12.21 | 
| 2017-08-28| BOX| 19.65 | 
| 2017-08-28| FB| 167.17 | 
| 2017-08-28| AMZN| 947.20 | 
| 2017-08-28| PCG| 70.28 | 
| 2017-08-28| AAPL| 161.48 | 
| 2017-08-28| AMC| 13.07 | 
| 2017-08-28| P| 8.15 | 
| 2017-08-28| WMT| 78.00 | 
| 2017-08-28| FDX| 208.80 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

