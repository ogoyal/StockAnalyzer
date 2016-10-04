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
| 2016-10-03| COST| 151.01| -1.50 | 
| 2016-10-03| ATVI| 44.001| -0.299 | 
| 2016-10-03| MSFT| 57.37| -0.23 | 
| 2016-10-03| GE| 29.64| +0.02 | 
| 2016-10-03| BA| 132.38| +0.64 | 
| 2016-10-03| AMD| 6.95| +0.04 | 
| 2016-10-03| UPS| 109.15| -0.21 | 
| 2016-10-03| FB| 128.77| +0.50 | 
| 2016-10-03| AMZN| 836.74| -0.57 | 
| 2016-10-03| PCG| 60.16| -1.01 | 
| 2016-10-03| AAPL| 112.52| -0.53 | 
| 2016-10-03| AMC| 32.22| +1.13 | 
| 2016-10-03| NFLX| 102.63| +4.08 | 
| 2016-10-03| WMT| 72.01| -0.11 | 
| 2016-10-03| FDX| 174.28| -0.40 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

