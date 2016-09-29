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
| 2016-09-28| COST| 149.64| -0.81 | 
| 2016-09-28| ATVI| 43.97| -0.24 | 
| 2016-09-28| MSFT| 57.995| +0.045 | 
| 2016-09-28| GE| 29.90| +0.02 | 
| 2016-09-28| BA| 132.23| +0.91 | 
| 2016-09-28| AMD| 6.55| +0.01 | 
| 2016-09-28| UPS| 109.25| -0.76 | 
| 2016-09-28| FB| 129.10| +0.41 | 
| 2016-09-27| AMZN| 816.11| +16.95 | 
| 2016-09-28| PCG| 62.38| +0.02 | 
| 2016-09-28| AAPL| 113.95| +0.86 | 
| 2016-09-28| AMC| 31.40| +0.08 | 
| 2016-09-28| NFLX| 97.48| +0.41 | 
| 2016-09-28| WMT| 71.71| -0.62 | 
| 2016-09-28| FDX| 175.68| -1.62 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

