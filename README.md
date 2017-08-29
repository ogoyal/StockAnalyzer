# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.26 | 
| 2017-08-29| ATVI| 63.28 | 
| 2017-08-29| MSFT| 72.88 | 
| 2017-08-29| GE| 24.39 | 
| 2017-08-29| BA| 239.00 | 
| 2017-08-29| AMD| 11.98 | 
| 2017-08-29| BOX| 19.37 | 
| 2017-08-29| FB| 167.99 | 
| 2017-08-29| AMZN| 952.69 | 
| 2017-08-29| PCG| 70.17 | 
| 2017-08-29| AAPL| 162.43 | 
| 2017-08-29| AMC| 12.62 | 
| 2017-08-29| P| 8.02 | 
| 2017-08-29| WMT| 78.66 | 
| 2017-08-29| FDX| 210.49 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

