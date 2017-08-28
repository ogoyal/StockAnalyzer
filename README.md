# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.05 | 
| 2017-08-28| ATVI| 62.61 | 
| 2017-08-28| MSFT| 72.77 | 
| 2017-08-28| GE| 24.43 | 
| 2017-08-28| BA| 236.85 | 
| 2017-08-28| AMD| 12.20 | 
| 2017-08-28| BOX| 19.79 | 
| 2017-08-28| FB| 167.13 | 
| 2017-08-28| AMZN| 948.80 | 
| 2017-08-28| PCG| 70.03 | 
| 2017-08-28| AAPL| 161.32 | 
| 2017-08-28| AMC| 13.07 | 
| 2017-08-28| P| 8.18 | 
| 2017-08-28| WMT| 77.97 | 
| 2017-08-28| FDX| 208.66 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

