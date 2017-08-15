# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-15| COST| 157.07 | 
| 2017-08-15| ATVI| 61.96 | 
| 2017-08-15| MSFT| 73.31 | 
| 2017-08-15| GE| 25.16 | 
| 2017-08-15| BA| 239.23 | 
| 2017-08-15| AMD| 13.04 | 
| 2017-08-15| BOX| 18.64 | 
| 2017-08-15| FB| 170.89 | 
| 2017-08-15| AMZN| 983.49 | 
| 2017-08-15| PCG| 69.23 | 
| 2017-08-15| AAPL| 161.80 | 
| 2017-08-15| AMC| 13.32 | 
| 2017-08-15| P| 8.41 | 
| 2017-08-15| WMT| 81.00 | 
| 2017-08-15| FDX| 209.51 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

