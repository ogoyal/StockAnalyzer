# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-23| COST| 159.03 | 
| 2017-08-23| ATVI| 63.91 | 
| 2017-08-23| MSFT| 72.88 | 
| 2017-08-23| GE| 24.38 | 
| 2017-08-23| BA| 237.93 | 
| 2017-08-23| AMD| 12.43 | 
| 2017-08-23| BOX| 19.56 | 
| 2017-08-23| FB| 169.05 | 
| 2017-08-23| AMZN| 957.87 | 
| 2017-08-23| PCG| 69.82 | 
| 2017-08-23| AAPL| 160.05 | 
| 2017-08-23| AMC| 12.52 | 
| 2017-08-23| P| 8.43 | 
| 2017-08-23| WMT| 80.01 | 
| 2017-08-23| FDX| 207.16 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

