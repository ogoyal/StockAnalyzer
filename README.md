# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-30| COST| 154.44 | 
| 2017-08-30| ATVI| 65.68 | 
| 2017-08-30| MSFT| 74.01 | 
| 2017-08-30| GE| 24.28 | 
| 2017-08-30| BA| 240.46 | 
| 2017-08-30| AMD| 12.67 | 
| 2017-08-30| BOX| 19.64 | 
| 2017-08-30| FB| 169.92 | 
| 2017-08-30| AMZN| 967.59 | 
| 2017-08-30| PCG| 70.11 | 
| 2017-08-30| AAPL| 163.35 | 
| 2017-08-30| AMC| 13.45 | 
| 2017-08-30| P| 8.08 | 
| 2017-08-30| WMT| 78.54 | 
| 2017-08-30| FDX| 213.78 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

