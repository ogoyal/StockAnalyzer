# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 156.46 | 
| 2017-08-31| ATVI| 65.48 | 
| 2017-08-31| MSFT| 74.82 | 
| 2017-08-31| GE| 24.60 | 
| 2017-08-31| BA| 239.42 | 
| 2017-08-31| AMD| 13.02 | 
| 2017-08-31| BOX| 19.51 | 
| 2017-08-31| FB| 171.83 | 
| 2017-08-31| AMZN| 978.67 | 
| 2017-08-31| PCG| 70.22 | 
| 2017-08-31| AAPL| 163.87 | 
| 2017-08-31| AMC| 13.35 | 
| 2017-08-31| P| 8.39 | 
| 2017-08-31| WMT| 78.29 | 
| 2017-08-31| FDX| 213.88 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

