# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-10| COST| 156.64 | 
| 2017-08-10| ATVI| 60.21 | 
| 2017-08-10| MSFT| 71.41 | 
| 2017-08-10| GE| 25.30 | 
| 2017-08-10| BA| 232.88 | 
| 2017-08-10| AMD| 12.12 | 
| 2017-08-10| BOX| 17.90 | 
| 2017-08-10| FB| 167.40 | 
| 2017-08-10| AMZN| 956.92 | 
| 2017-08-10| PCG| 69.13 | 
| 2017-08-10| AAPL| 155.27 | 
| 2017-08-10| AMC| 14.45 | 
| 2017-08-10| P| 7.99 | 
| 2017-08-10| WMT| 80.66 | 
| 2017-08-10| FDX| 203.55 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

