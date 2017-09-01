# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-09-01| COST| 158.32 | 
| 2017-09-01| ATVI| 65.02 | 
| 2017-09-01| MSFT| 73.85 | 
| 2017-09-01| GE| 25.15 | 
| 2017-09-01| BA| 242.47 | 
| 2017-09-01| AMD| 13.24 | 
| 2017-09-01| BOX| 19.31 | 
| 2017-09-01| FB| 172.57 | 
| 2017-09-01| AMZN| 981.86 | 
| 2017-09-01| PCG| 69.89 | 
| 2017-09-01| AAPL| 164.02 | 
| 2017-09-01| AMC| 14.10 | 
| 2017-09-01| P| 8.46 | 
| 2017-09-01| WMT| 78.24 | 
| 2017-09-01| FDX| 216.65 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

