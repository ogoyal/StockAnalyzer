# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.06 | 
| 2017-08-28| ATVI| 62.48 | 
| 2017-08-28| MSFT| 72.71 | 
| 2017-08-28| GE| 24.40 | 
| 2017-08-28| BA| 236.49 | 
| 2017-08-28| AMD| 12.19 | 
| 2017-08-28| BOX| 19.67 | 
| 2017-08-28| FB| 166.92 | 
| 2017-08-28| AMZN| 946.73 | 
| 2017-08-28| PCG| 70.22 | 
| 2017-08-28| AAPL| 161.30 | 
| 2017-08-28| AMC| 13.18 | 
| 2017-08-28| P| 8.15 | 
| 2017-08-28| WMT| 77.98 | 
| 2017-08-28| FDX| 208.76 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

