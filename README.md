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
| 2017-08-28| ATVI| 62.61 | 
| 2017-08-28| MSFT| 72.73 | 
| 2017-08-28| GE| 24.50 | 
| 2017-08-28| BA| 235.26 | 
| 2017-08-28| AMD| 12.27 | 
| 2017-08-28| BOX| 19.67 | 
| 2017-08-28| FB| 166.95 | 
| 2017-08-28| AMZN| 950.91 | 
| 2017-08-28| PCG| 70.26 | 
| 2017-08-28| AAPL| 161.49 | 
| 2017-08-28| AMC| 12.93 | 
| 2017-08-28| P| 8.09 | 
| 2017-08-28| WMT| 78.10 | 
| 2017-08-28| FDX| 208.83 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

