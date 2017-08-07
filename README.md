# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 156.40 | 
| 2017-08-07| ATVI| 62.78 | 
| 2017-08-07| MSFT| 72.38 | 
| 2017-08-07| GE| 25.61 | 
| 2017-08-07| BA| 241.25 | 
| 2017-08-07| AMD| 13.39 | 
| 2017-08-07| BOX| 18.92 | 
| 2017-08-07| FB| 171.46 | 
| 2017-08-07| AMZN| 990.93 | 
| 2017-08-07| PCG| 68.62 | 
| 2017-08-07| AAPL| 157.88 | 
| 2017-08-07| AMC| 16.17 | 
| 2017-08-07| P| 8.64 | 
| 2017-08-07| WMT| 81.18 | 
| 2017-08-07| FDX| 208.45 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

