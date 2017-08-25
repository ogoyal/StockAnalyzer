# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.55 | 
| 2017-08-25| ATVI| 62.66 | 
| 2017-08-25| MSFT| 73.02 | 
| 2017-08-25| GE| 24.58 | 
| 2017-08-25| BA| 236.61 | 
| 2017-08-25| AMD| 12.40 | 
| 2017-08-25| BOX| 19.61 | 
| 2017-08-25| FB| 166.48 | 
| 2017-08-25| AMZN| 946.51 | 
| 2017-08-25| PCG| 70.27 | 
| 2017-08-25| AAPL| 160.05 | 
| 2017-08-25| AMC| 12.95 | 
| 2017-08-25| P| 8.08 | 
| 2017-08-25| WMT| 78.96 | 
| 2017-08-25| FDX| 208.37 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

