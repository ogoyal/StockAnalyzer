# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.55 | 
| 2017-08-28| ATVI| 62.75 | 
| 2017-08-28| MSFT| 72.83 | 
| 2017-08-28| GE| 24.47 | 
| 2017-08-28| BA| 237.18 | 
| 2017-08-28| AMD| 12.23 | 
| 2017-08-28| BOX| 19.62 | 
| 2017-08-28| FB| 167.24 | 
| 2017-08-28| AMZN| 946.02 | 
| 2017-08-28| PCG| 70.31 | 
| 2017-08-28| AAPL| 161.47 | 
| 2017-08-28| AMC| 13.05 | 
| 2017-08-28| P| 8.18 | 
| 2017-08-28| WMT| 78.03 | 
| 2017-08-28| FDX| 208.84 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

