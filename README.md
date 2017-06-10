# CSVTableContainer
C++ Program using Standard Library

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.
Creates a C++ program to do data analytics.

Sample CSV data file:

| Date| Stocks| Price($)| Change($) | 
| --- | --- | --- | ---  | 
| 2017-06-09| COST| 64.45| +1.24 | 
| 2017-06-09| ATVI| 59.21| -0.94 | 
| 2017-06-09| MSFT| 22.70| +0.93 | 
| 2017-06-09| GE| 27.09| -0.15 | 
| 2017-06-09| BA| 59.91| +0.31 | 
| 2017-06-09| AMD| 59.21| -0.94 | 
| ---| UPS| |  | 
| 2017-06-09| FB| 11.13| +0.03 | 
| 2017-06-09| AMZN| 59.21| -0.94 | 
| 2017-06-09| PCG| 8.52| +0.10 | 
| 2017-06-09| AAPL| 59.21| -0.94 | 
| 2017-06-09| AMC| 59.21| -0.94 | 
| 2016-11-04| NFLX| 90.34| +0.00 | 
| 2017-06-09| WMT| 70.07| -3.09 | 
| 2017-06-09| FDX| 11.13| +0.03 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

