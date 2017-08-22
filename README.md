# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 159.04 | 
| 2017-08-22| ATVI| 63.17 | 
| 2017-08-22| MSFT| 72.96 | 
| 2017-08-22| GE| 24.66 | 
| 2017-08-22| BA| 238.80 | 
| 2017-08-22| AMD| 12.28 | 
| 2017-08-22| BOX| 19.31 | 
| 2017-08-22| FB| 168.68 | 
| 2017-08-22| AMZN| 963.93 | 
| 2017-08-22| PCG| 69.40 | 
| 2017-08-22| AAPL| 159.41 | 
| 2017-08-22| AMC| 13.07 | 
| 2017-08-22| P| 8.39 | 
| 2017-08-22| WMT| 80.09 | 
| 2017-08-22| FDX| 207.80 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

