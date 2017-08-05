# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-04| COST| 156.44 | 
| 2017-08-04| ATVI| 62.01 | 
| 2017-08-04| MSFT| 72.68 | 
| 2017-08-04| GE| 25.78 | 
| 2017-08-04| BA| 237.71 | 
| 2017-08-04| AMD| 13.12 | 
| 2017-08-04| BOX| 18.69 | 
| 2017-08-04| FB| 169.62 | 
| 2017-08-04| AMZN| 987.58 | 
| 2017-08-04| PCG| 68.55 | 
| 2017-08-04| AAPL| 156.39 | 
| 2017-08-04| AMC| 16.25 | 
| 2017-08-04| P| 8.48 | 
| 2017-08-04| WMT| 80.48 | 
| 2017-08-04| FDX| 209.32 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

