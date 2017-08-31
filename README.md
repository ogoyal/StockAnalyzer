# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 156.84 | 
| 2017-08-31| ATVI| 65.57 | 
| 2017-08-31| MSFT| 74.82 | 
| 2017-08-31| GE| 24.60 | 
| 2017-08-31| BA| 239.57 | 
| 2017-08-31| AMD| 12.99 | 
| 2017-08-31| BOX| 19.66 | 
| 2017-08-31| FB| 171.81 | 
| 2017-08-31| AMZN| 980.31 | 
| 2017-08-31| PCG| 70.34 | 
| 2017-08-31| AAPL| 164.15 | 
| 2017-08-31| AMC| 13.38 | 
| 2017-08-31| P| 8.45 | 
| 2017-08-31| WMT| 78.09 | 
| 2017-08-31| FDX| 214.54 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

