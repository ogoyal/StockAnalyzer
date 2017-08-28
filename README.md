# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.10 | 
| 2017-08-28| ATVI| 62.54 | 
| 2017-08-28| MSFT| 72.70 | 
| 2017-08-28| GE| 24.39 | 
| 2017-08-28| BA| 236.68 | 
| 2017-08-28| AMD| 12.17 | 
| 2017-08-28| BOX| 19.65 | 
| 2017-08-28| FB| 166.87 | 
| 2017-08-28| AMZN| 947.25 | 
| 2017-08-28| PCG| 70.11 | 
| 2017-08-28| AAPL| 161.10 | 
| 2017-08-28| AMC| 13.10 | 
| 2017-08-28| P| 8.15 | 
| 2017-08-28| WMT| 77.97 | 
| 2017-08-28| FDX| 208.79 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

