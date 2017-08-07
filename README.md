# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 156.93 | 
| 2017-08-07| ATVI| 62.33 | 
| 2017-08-07| MSFT| 72.31 | 
| 2017-08-07| GE| 25.58 | 
| 2017-08-07| BA| 240.18 | 
| 2017-08-07| AMD| 13.38 | 
| 2017-08-07| BOX| 18.76 | 
| 2017-08-07| FB| 171.47 | 
| 2017-08-07| AMZN| 991.05 | 
| 2017-08-07| PCG| 68.70 | 
| 2017-08-07| AAPL| 158.63 | 
| 2017-08-07| AMC| 16.23 | 
| 2017-08-07| P| 8.59 | 
| 2017-08-07| WMT| 81.40 | 
| 2017-08-07| FDX| 208.72 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

