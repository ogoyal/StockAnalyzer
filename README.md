# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 158.81 | 
| 2017-08-22| ATVI| 64.26 | 
| 2017-08-22| MSFT| 73.19 | 
| 2017-08-22| GE| 24.64 | 
| 2017-08-22| BA| 239.79 | 
| 2017-08-22| AMD| 12.17 | 
| 2017-08-22| BOX| 19.40 | 
| 2017-08-22| FB| 169.62 | 
| 2017-08-22| AMZN| 967.25 | 
| 2017-08-22| PCG| 69.59 | 
| 2017-08-22| AAPL| 159.90 | 
| 2017-08-22| AMC| 12.88 | 
| 2017-08-22| P| 8.59 | 
| 2017-08-22| WMT| 79.99 | 
| 2017-08-22| FDX| 209.42 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

