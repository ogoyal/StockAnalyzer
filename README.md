# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 158.71 | 
| 2017-08-22| ATVI| 63.84 | 
| 2017-08-22| MSFT| 73.14 | 
| 2017-08-22| GE| 24.55 | 
| 2017-08-22| BA| 239.69 | 
| 2017-08-22| AMD| 12.19 | 
| 2017-08-22| BOX| 19.35 | 
| 2017-08-22| FB| 169.55 | 
| 2017-08-22| AMZN| 966.25 | 
| 2017-08-22| PCG| 69.54 | 
| 2017-08-22| AAPL| 159.90 | 
| 2017-08-22| AMC| 12.60 | 
| 2017-08-22| P| 8.52 | 
| 2017-08-22| WMT| 80.02 | 
| 2017-08-22| FDX| 209.37 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

