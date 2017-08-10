# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-10| COST| 156.75 | 
| 2017-08-10| ATVI| 60.44 | 
| 2017-08-10| MSFT| 71.80 | 
| 2017-08-10| GE| 25.47 | 
| 2017-08-10| BA| 233.16 | 
| 2017-08-10| AMD| 12.23 | 
| 2017-08-10| BOX| 17.97 | 
| 2017-08-10| FB| 167.62 | 
| 2017-08-10| AMZN| 959.49 | 
| 2017-08-10| PCG| 69.09 | 
| 2017-08-10| AAPL| 157.39 | 
| 2017-08-10| AMC| 14.60 | 
| 2017-08-10| P| 8.14 | 
| 2017-08-10| WMT| 80.83 | 
| 2017-08-10| FDX| 204.91 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

