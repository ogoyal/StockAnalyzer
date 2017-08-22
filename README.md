# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 158.92 | 
| 2017-08-22| ATVI| 63.92 | 
| 2017-08-22| MSFT| 72.91 | 
| 2017-08-22| GE| 24.63 | 
| 2017-08-22| BA| 238.91 | 
| 2017-08-22| AMD| 12.18 | 
| 2017-08-22| BOX| 19.19 | 
| 2017-08-22| FB| 169.20 | 
| 2017-08-22| AMZN| 965.67 | 
| 2017-08-22| PCG| 69.55 | 
| 2017-08-22| AAPL| 159.64 | 
| 2017-08-22| AMC| 12.68 | 
| 2017-08-22| P| 8.43 | 
| 2017-08-22| WMT| 79.97 | 
| 2017-08-22| FDX| 208.90 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

