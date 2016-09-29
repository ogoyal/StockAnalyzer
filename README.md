# CSVTableContainer
C++ Program using Standard Library

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.
Creates a C++ program to do data analytics.

Sample CSV data file:

| Date| Stocks| Price| Change | 
| --- | --- | --- | ---  | 
| 2016-09-28| COST| 149.41| -1.04 | 
| 2016-09-28| ATVI| 44.16| -0.05 | 
| 2016-09-27| MSFT| 57.95| +1.05 | 
| 2016-09-28| GE| 29.90| +0.02 | 
| 2016-09-28| BA| 132.23| +0.91 | 
| 2016-09-28| AMD| 6.59| +0.05 | 
| 2016-09-28| UPS| 109.25| -0.76 | 
| 2016-09-28| FB| 129.23| +0.54 | 
| 2016-09-28| AMZN| 827.48| +11.37 | 
| 2016-09-28| PCG| 62.38| +0.02 | 
| 2016-09-28| AAPL| 114.01| +0.92 | 
| 2016-09-28| AMC| 31.31| -0.01 | 
| 2016-09-28| NFLX| 97.48| +0.41 | 
| 2016-09-28| WMT| 71.71| -0.62 | 
| 2016-09-28| FDX| 175.45| -1.85 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

