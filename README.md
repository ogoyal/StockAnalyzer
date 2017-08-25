# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 150.88 | 
| 2017-08-25| ATVI| 62.61 | 
| 2017-08-25| MSFT| 72.57 | 
| 2017-08-25| GE| 24.53 | 
| 2017-08-25| BA| 236.83 | 
| 2017-08-25| AMD| 12.32 | 
| 2017-08-25| BOX| 19.75 | 
| 2017-08-25| FB| 166.50 | 
| 2017-08-25| AMZN| 949.96 | 
| 2017-08-25| PCG| 70.15 | 
| 2017-08-25| AAPL| 159.65 | 
| 2017-08-25| AMC| 13.10 | 
| 2017-08-25| P| 8.21 | 
| 2017-08-25| WMT| 78.62 | 
| 2017-08-25| FDX| 207.58 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

