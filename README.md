# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 155.86 | 
| 2017-08-07| ATVI| 62.04 | 
| 2017-08-07| MSFT| 72.55 | 
| 2017-08-07| GE| 25.57 | 
| 2017-08-07| BA| 239.05 | 
| 2017-08-07| AMD| 13.40 | 
| 2017-08-07| BOX| 18.75 | 
| 2017-08-07| FB| 171.12 | 
| 2017-08-07| AMZN| 992.99 | 
| 2017-08-07| PCG| 68.73 | 
| 2017-08-07| AAPL| 157.60 | 
| 2017-08-07| AMC| 16.25 | 
| 2017-08-07| P| 8.48 | 
| 2017-08-07| WMT| 80.98 | 
| 2017-08-07| FDX| 207.88 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

