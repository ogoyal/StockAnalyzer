# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-17| COST| 158.93 | 
| 2017-08-17| ATVI| 62.11 | 
| 2017-08-17| MSFT| 73.02 | 
| 2017-08-17| GE| 24.94 | 
| 2017-08-17| BA| 236.10 | 
| 2017-08-17| AMD| 12.52 | 
| 2017-08-17| BOX| 18.80 | 
| 2017-08-17| FB| 168.41 | 
| 2017-08-17| AMZN| 965.03 | 
| 2017-08-17| PCG| 69.23 | 
| 2017-08-17| AAPL| 158.78 | 
| 2017-08-17| AMC| 13.38 | 
| 2017-08-17| P| 8.51 | 
| 2017-08-17| WMT| 78.96 | 
| 2017-08-17| FDX| 206.65 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

