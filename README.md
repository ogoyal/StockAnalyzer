# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-25| COST| 152.45 | 
| 2017-08-25| ATVI| 62.58 | 
| 2017-08-25| MSFT| 72.82 | 
| 2017-08-25| GE| 24.49 | 
| 2017-08-25| BA| 235.89 | 
| 2017-08-25| AMD| 12.43 | 
| 2017-08-25| BOX| 19.58 | 
| 2017-08-25| FB| 166.32 | 
| 2017-08-25| AMZN| 945.26 | 
| 2017-08-25| PCG| 70.08 | 
| 2017-08-25| AAPL| 159.86 | 
| 2017-08-25| AMC| 12.90 | 
| 2017-08-25| P| 8.08 | 
| 2017-08-25| WMT| 78.63 | 
| 2017-08-25| FDX| 207.76 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

