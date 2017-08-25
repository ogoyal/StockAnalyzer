# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-24| COST| 151.33 | 
| 2017-08-24| ATVI| 63.43 | 
| 2017-08-24| MSFT| 72.69 | 
| 2017-08-24| GE| 24.30 | 
| 2017-08-24| BA| 238.74 | 
| 2017-08-24| AMD| 12.50 | 
| 2017-08-24| BOX| 19.74 | 
| 2017-08-24| FB| 167.74 | 
| 2017-08-24| AMZN| 952.45 | 
| 2017-08-24| PCG| 69.78 | 
| 2017-08-24| AAPL| 159.27 | 
| 2017-08-24| AMC| 12.80 | 
| 2017-08-24| P| 8.38 | 
| 2017-08-24| WMT| 78.34 | 
| 2017-08-24| FDX| 206.67 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

