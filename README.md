# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 158.73 | 
| 2017-08-22| ATVI| 64.05 | 
| 2017-08-22| MSFT| 72.96 | 
| 2017-08-22| GE| 24.57 | 
| 2017-08-22| BA| 239.06 | 
| 2017-08-22| AMD| 12.15 | 
| 2017-08-22| BOX| 19.27 | 
| 2017-08-22| FB| 169.37 | 
| 2017-08-22| AMZN| 965.14 | 
| 2017-08-22| PCG| 69.59 | 
| 2017-08-22| AAPL| 159.80 | 
| 2017-08-22| AMC| 12.65 | 
| 2017-08-22| P| 8.49 | 
| 2017-08-22| WMT| 79.96 | 
| 2017-08-22| FDX| 208.94 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

