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
| 2017-06-13| COST| 64.9821| +0.6621 | 
| 2017-06-13| ATVI| 59.25| +0.26 | 
| 2017-06-13| MSFT| 22.24| -0.05 | 
| 2017-06-13| GE| 27.45| +0.32 | 
| 2017-06-13| BA| 59.14| -0.22 | 
| 2017-06-13| AMD| 59.25| +0.26 | 
| ---| UPS| |  | 
| 2017-06-13| FB| 11.28| +0.00 | 
| 2017-06-13| AMZN| 59.20| +0.21 | 
| 2017-06-13| PCG| 7.96| +0.09 | 
| 2017-06-13| AAPL| 59.25| +0.26 | 
| 2017-06-13| AMC| 59.20| +0.21 | 
| 2016-11-04| NFLX| 90.34| +0.00 | 
| 2017-06-13| WMT| 70.56| +0.01 | 
| 2017-06-13| FDX| 11.28| +0.00 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

