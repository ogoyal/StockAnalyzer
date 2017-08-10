# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-10| COST| 156.85 | 
| 2017-08-10| ATVI| 60.45 | 
| 2017-08-10| MSFT| 71.58 | 
| 2017-08-10| GE| 25.30 | 
| 2017-08-10| BA| 233.30 | 
| 2017-08-10| AMD| 12.19 | 
| 2017-08-10| BOX| 18.01 | 
| 2017-08-10| FB| 167.57 | 
| 2017-08-10| AMZN| 957.40 | 
| 2017-08-10| PCG| 69.04 | 
| 2017-08-10| AAPL| 155.87 | 
| 2017-08-10| AMC| 14.52 | 
| 2017-08-10| P| 8.10 | 
| 2017-08-10| WMT| 80.86 | 
| 2017-08-10| FDX| 204.31 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

