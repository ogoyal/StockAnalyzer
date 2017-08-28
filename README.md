# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-28| COST| 152.75 | 
| 2017-08-28| ATVI| 62.70 | 
| 2017-08-28| MSFT| 72.86 | 
| 2017-08-28| GE| 24.49 | 
| 2017-08-28| BA| 235.67 | 
| 2017-08-28| AMD| 12.18 | 
| 2017-08-28| BOX| 19.91 | 
| 2017-08-28| FB| 167.46 | 
| 2017-08-28| AMZN| 951.97 | 
| 2017-08-28| PCG| 70.10 | 
| 2017-08-28| AAPL| 161.94 | 
| 2017-08-28| AMC| 12.98 | 
| 2017-08-28| P| 8.15 | 
| 2017-08-28| WMT| 78.10 | 
| 2017-08-28| FDX| 208.27 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

