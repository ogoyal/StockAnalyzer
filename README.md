# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 159.09 | 
| 2017-08-22| ATVI| 63.73 | 
| 2017-08-22| MSFT| 73.00 | 
| 2017-08-22| GE| 24.65 | 
| 2017-08-22| BA| 238.98 | 
| 2017-08-22| AMD| 12.29 | 
| 2017-08-22| BOX| 19.21 | 
| 2017-08-22| FB| 169.38 | 
| 2017-08-22| AMZN| 965.66 | 
| 2017-08-22| PCG| 69.44 | 
| 2017-08-22| AAPL| 159.84 | 
| 2017-08-22| AMC| 12.75 | 
| 2017-08-22| P| 8.40 | 
| 2017-08-22| WMT| 80.01 | 
| 2017-08-22| FDX| 209.08 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

