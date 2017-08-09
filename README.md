# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-08| COST| 157.75 | 
| 2017-08-08| ATVI| 61.33 | 
| 2017-08-08| MSFT| 72.79 | 
| 2017-08-08| GE| 25.56 | 
| 2017-08-08| BA| 239.50 | 
| 2017-08-08| AMD| 13.11 | 
| 2017-08-08| BOX| 18.77 | 
| 2017-08-08| FB| 171.23 | 
| 2017-08-08| AMZN| 989.84 | 
| 2017-08-08| PCG| 69.25 | 
| 2017-08-08| AAPL| 160.08 | 
| 2017-08-08| AMC| 16.15 | 
| 2017-08-08| P| 8.65 | 
| 2017-08-08| WMT| 81.59 | 
| 2017-08-08| FDX| 207.00 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

