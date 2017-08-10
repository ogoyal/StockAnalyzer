# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-09| COST| 156.86 | 
| 2017-08-09| ATVI| 61.38 | 
| 2017-08-09| MSFT| 72.47 | 
| 2017-08-09| GE| 25.71 | 
| 2017-08-09| BA| 234.31 | 
| 2017-08-09| AMD| 12.83 | 
| 2017-08-09| BOX| 18.80 | 
| 2017-08-09| FB| 171.18 | 
| 2017-08-09| AMZN| 982.01 | 
| 2017-08-09| PCG| 69.02 | 
| 2017-08-09| AAPL| 161.06 | 
| 2017-08-09| AMC| 15.50 | 
| 2017-08-09| P| 8.55 | 
| 2017-08-09| WMT| 81.61 | 
| 2017-08-09| FDX| 206.18 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

