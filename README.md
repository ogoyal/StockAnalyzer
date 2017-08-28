# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 151.88 | 
| 2017-08-28| ATVI| 62.58 | 
| 2017-08-28| MSFT| 72.69 | 
| 2017-08-28| GE| 24.40 | 
| 2017-08-28| BA| 236.98 | 
| 2017-08-28| AMD| 12.24 | 
| 2017-08-28| BOX| 19.64 | 
| 2017-08-28| FB| 167.08 | 
| 2017-08-28| AMZN| 947.54 | 
| 2017-08-28| PCG| 70.21 | 
| 2017-08-28| AAPL| 161.52 | 
| 2017-08-28| AMC| 13.12 | 
| 2017-08-28| P| 8.14 | 
| 2017-08-28| WMT| 77.88 | 
| 2017-08-28| FDX| 208.79 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

