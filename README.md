# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-23| COST| 158.70 | 
| 2017-08-23| ATVI| 64.06 | 
| 2017-08-23| MSFT| 72.72 | 
| 2017-08-23| GE| 24.40 | 
| 2017-08-23| BA| 237.71 | 
| 2017-08-23| AMD| 12.51 | 
| 2017-08-23| BOX| 19.53 | 
| 2017-08-23| FB| 169.00 | 
| 2017-08-23| AMZN| 960.15 | 
| 2017-08-23| PCG| 69.65 | 
| 2017-08-23| AAPL| 160.41 | 
| 2017-08-23| AMC| 12.62 | 
| 2017-08-23| P| 8.54 | 
| 2017-08-23| WMT| 80.14 | 
| 2017-08-23| FDX| 206.66 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

