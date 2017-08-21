# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-21| COST| 157.80 | 
| 2017-08-21| ATVI| 61.82 | 
| 2017-08-21| MSFT| 72.14 | 
| 2017-08-21| GE| 24.52 | 
| 2017-08-21| BA| 235.63 | 
| 2017-08-21| AMD| 12.02 | 
| 2017-08-21| BOX| 18.85 | 
| 2017-08-21| FB| 167.52 | 
| 2017-08-21| AMZN| 952.85 | 
| 2017-08-21| PCG| 69.33 | 
| 2017-08-21| AAPL| 157.03 | 
| 2017-08-21| AMC| 12.68 | 
| 2017-08-21| P| 8.14 | 
| 2017-08-21| WMT| 79.72 | 
| 2017-08-21| FDX| 205.85 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

