# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.12 | 
| 2017-08-21| ATVI| 61.65 | 
| 2017-08-21| MSFT| 71.93 | 
| 2017-08-21| GE| 24.52 | 
| 2017-08-21| BA| 234.86 | 
| 2017-08-21| AMD| 11.98 | 
| 2017-08-21| BOX| 18.89 | 
| 2017-08-21| FB| 167.40 | 
| 2017-08-21| AMZN| 949.62 | 
| 2017-08-21| PCG| 69.34 | 
| 2017-08-21| AAPL| 156.75 | 
| 2017-08-21| AMC| 12.90 | 
| 2017-08-21| P| 8.10 | 
| 2017-08-21| WMT| 79.76 | 
| 2017-08-21| FDX| 205.91 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

