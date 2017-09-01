# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.12 | 
| 2017-09-01| ATVI| 65.04 | 
| 2017-09-01| MSFT| 74.07 | 
| 2017-09-01| GE| 25.24 | 
| 2017-09-01| BA| 241.30 | 
| 2017-09-01| AMD| 13.10 | 
| 2017-09-01| BOX| 19.03 | 
| 2017-09-01| FB| 171.95 | 
| 2017-09-01| AMZN| 978.81 | 
| 2017-09-01| PCG| 69.93 | 
| 2017-09-01| AAPL| 163.90 | 
| 2017-09-01| AMC| 14.27 | 
| 2017-09-01| P| 8.33 | 
| 2017-09-01| WMT| 78.31 | 
| 2017-09-01| FDX| 216.03 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

