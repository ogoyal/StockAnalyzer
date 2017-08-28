# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 151.81 | 
| 2017-08-28| ATVI| 62.69 | 
| 2017-08-28| MSFT| 72.62 | 
| 2017-08-28| GE| 24.45 | 
| 2017-08-28| BA| 237.12 | 
| 2017-08-28| AMD| 12.22 | 
| 2017-08-28| BOX| 19.64 | 
| 2017-08-28| FB| 166.87 | 
| 2017-08-28| AMZN| 946.51 | 
| 2017-08-28| PCG| 70.22 | 
| 2017-08-28| AAPL| 161.27 | 
| 2017-08-28| AMC| 12.98 | 
| 2017-08-28| P| 8.16 | 
| 2017-08-28| WMT| 77.97 | 
| 2017-08-28| FDX| 208.96 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

