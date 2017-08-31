# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 156.74 | 
| 2017-08-31| ATVI| 65.56 | 
| 2017-08-31| MSFT| 74.77 | 
| 2017-08-31| GE| 24.55 | 
| 2017-08-31| BA| 239.66 | 
| 2017-08-31| AMD| 13.00 | 
| 2017-08-31| BOX| 19.62 | 
| 2017-08-31| FB| 171.97 | 
| 2017-08-31| AMZN| 980.60 | 
| 2017-08-31| PCG| 70.38 | 
| 2017-08-31| AAPL| 164.00 | 
| 2017-08-31| AMC| 13.40 | 
| 2017-08-31| P| 8.45 | 
| 2017-08-31| WMT| 78.07 | 
| 2017-08-31| FDX| 214.38 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

