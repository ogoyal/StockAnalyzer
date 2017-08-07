# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-07| COST| 155.34 | 
| 2017-08-07| ATVI| 62.44 | 
| 2017-08-07| MSFT| 72.75 | 
| 2017-08-07| GE| 25.57 | 
| 2017-08-07| BA| 239.67 | 
| 2017-08-07| AMD| 13.34 | 
| 2017-08-07| BOX| 18.84 | 
| 2017-08-07| FB| 171.10 | 
| 2017-08-07| AMZN| 992.29 | 
| 2017-08-07| PCG| 68.66 | 
| 2017-08-07| AAPL| 157.62 | 
| 2017-08-07| AMC| 16.10 | 
| 2017-08-07| P| 8.53 | 
| 2017-08-07| WMT| 80.85 | 
| 2017-08-07| FDX| 207.93 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

