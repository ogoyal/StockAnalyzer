# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.19 | 
| 2017-08-28| ATVI| 62.71 | 
| 2017-08-28| MSFT| 72.88 | 
| 2017-08-28| GE| 24.46 | 
| 2017-08-28| BA| 236.77 | 
| 2017-08-28| AMD| 12.18 | 
| 2017-08-28| BOX| 19.81 | 
| 2017-08-28| FB| 167.48 | 
| 2017-08-28| AMZN| 950.06 | 
| 2017-08-28| PCG| 70.10 | 
| 2017-08-28| AAPL| 161.59 | 
| 2017-08-28| AMC| 13.12 | 
| 2017-08-28| P| 8.16 | 
| 2017-08-28| WMT| 78.09 | 
| 2017-08-28| FDX| 208.73 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

