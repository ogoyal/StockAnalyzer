# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 155.99 | 
| 2017-08-31| ATVI| 65.60 | 
| 2017-08-31| MSFT| 74.67 | 
| 2017-08-31| GE| 24.57 | 
| 2017-08-31| BA| 239.18 | 
| 2017-08-31| AMD| 12.94 | 
| 2017-08-31| BOX| 19.36 | 
| 2017-08-31| FB| 171.51 | 
| 2017-08-31| AMZN| 978.37 | 
| 2017-08-31| PCG| 70.21 | 
| 2017-08-31| AAPL| 163.85 | 
| 2017-08-31| AMC| 13.35 | 
| 2017-08-31| P| 8.40 | 
| 2017-08-31| WMT| 78.48 | 
| 2017-08-31| FDX| 213.74 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

