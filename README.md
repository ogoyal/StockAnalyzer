# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-15| COST| 156.88 | 
| 2017-08-15| ATVI| 61.97 | 
| 2017-08-15| MSFT| 73.22 | 
| 2017-08-15| GE| 25.14 | 
| 2017-08-15| BA| 239.17 | 
| 2017-08-15| AMD| 13.02 | 
| 2017-08-15| BOX| 18.61 | 
| 2017-08-15| FB| 171.00 | 
| 2017-08-15| AMZN| 982.74 | 
| 2017-08-15| PCG| 69.35 | 
| 2017-08-15| AAPL| 161.60 | 
| 2017-08-15| AMC| 13.25 | 
| 2017-08-15| P| 8.40 | 
| 2017-08-15| WMT| 80.77 | 
| 2017-08-15| FDX| 209.07 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

