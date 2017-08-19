# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-18| COST| 157.08 | 
| 2017-08-18| ATVI| 62.01 | 
| 2017-08-18| MSFT| 72.49 | 
| 2017-08-18| GE| 24.55 | 
| 2017-08-18| BA| 235.77 | 
| 2017-08-18| AMD| 12.37 | 
| 2017-08-18| BOX| 18.75 | 
| 2017-08-18| FB| 167.41 | 
| 2017-08-18| AMZN| 958.47 | 
| 2017-08-18| PCG| 69.14 | 
| 2017-08-18| AAPL| 157.50 | 
| 2017-08-18| AMC| 13.00 | 
| 2017-08-18| P| 8.27 | 
| 2017-08-18| WMT| 79.31 | 
| 2017-08-18| FDX| 206.00 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

