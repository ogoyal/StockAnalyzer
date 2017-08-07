# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 156.95 | 
| 2017-08-07| ATVI| 62.51 | 
| 2017-08-07| MSFT| 72.40 | 
| 2017-08-07| GE| 25.63 | 
| 2017-08-07| BA| 240.23 | 
| 2017-08-07| AMD| 13.43 | 
| 2017-08-07| BOX| 18.84 | 
| 2017-08-07| FB| 171.98 | 
| 2017-08-07| AMZN| 992.27 | 
| 2017-08-07| PCG| 68.94 | 
| 2017-08-07| AAPL| 158.59 | 
| 2017-08-07| AMC| 16.10 | 
| 2017-08-07| P| 8.60 | 
| 2017-08-07| WMT| 81.28 | 
| 2017-08-07| FDX| 208.37 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

