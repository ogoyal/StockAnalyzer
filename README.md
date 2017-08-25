# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.50 | 
| 2017-08-25| ATVI| 62.69 | 
| 2017-08-25| MSFT| 72.89 | 
| 2017-08-25| GE| 24.52 | 
| 2017-08-25| BA| 236.02 | 
| 2017-08-25| AMD| 12.41 | 
| 2017-08-25| BOX| 19.58 | 
| 2017-08-25| FB| 166.44 | 
| 2017-08-25| AMZN| 944.30 | 
| 2017-08-25| PCG| 70.12 | 
| 2017-08-25| AAPL| 159.90 | 
| 2017-08-25| AMC| 12.90 | 
| 2017-08-25| P| 8.07 | 
| 2017-08-25| WMT| 78.76 | 
| 2017-08-25| FDX| 208.11 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

