# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-29| COST| 153.49 | 
| 2017-08-29| ATVI| 63.74 | 
| 2017-08-29| MSFT| 73.02 | 
| 2017-08-29| GE| 24.36 | 
| 2017-08-29| BA| 239.57 | 
| 2017-08-29| AMD| 12.12 | 
| 2017-08-29| BOX| 19.40 | 
| 2017-08-29| FB| 167.89 | 
| 2017-08-29| AMZN| 953.52 | 
| 2017-08-29| PCG| 70.18 | 
| 2017-08-29| AAPL| 162.51 | 
| 2017-08-29| AMC| 12.57 | 
| 2017-08-29| P| 8.10 | 
| 2017-08-29| WMT| 78.74 | 
| 2017-08-29| FDX| 210.80 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

