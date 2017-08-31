# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 156.97 | 
| 2017-08-31| ATVI| 65.50 | 
| 2017-08-31| MSFT| 74.85 | 
| 2017-08-31| GE| 24.66 | 
| 2017-08-31| BA| 239.56 | 
| 2017-08-31| AMD| 13.02 | 
| 2017-08-31| BOX| 19.36 | 
| 2017-08-31| FB| 171.99 | 
| 2017-08-31| AMZN| 980.24 | 
| 2017-08-31| PCG| 70.30 | 
| 2017-08-31| AAPL| 164.12 | 
| 2017-08-31| AMC| 13.35 | 
| 2017-08-31| P| 8.38 | 
| 2017-08-31| WMT| 78.27 | 
| 2017-08-31| FDX| 214.49 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

