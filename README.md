# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 156.07 | 
| 2017-08-07| ATVI| 62.58 | 
| 2017-08-07| MSFT| 72.47 | 
| 2017-08-07| GE| 25.60 | 
| 2017-08-07| BA| 240.01 | 
| 2017-08-07| AMD| 13.44 | 
| 2017-08-07| BOX| 18.86 | 
| 2017-08-07| FB| 171.42 | 
| 2017-08-07| AMZN| 993.83 | 
| 2017-08-07| PCG| 68.60 | 
| 2017-08-07| AAPL| 157.76 | 
| 2017-08-07| AMC| 16.10 | 
| 2017-08-07| P| 8.60 | 
| 2017-08-07| WMT| 81.07 | 
| 2017-08-07| FDX| 207.95 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

