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
| 2016-09-26| COST| 151.31| -1.22 | 
| 2016-09-26| ATVI| 43.98| -0.38 | 
| 2016-09-23| MSFT| 57.43| -0.39 | 
| 2016-09-26| GE| 29.605| -0.285 | 
| 2016-09-26| BA| 130.92| -0.86 | 
| 2016-09-26| AMD| 6.32| -0.23 | 
| 2016-09-26| UPS| 108.89| -0.32 | 
| 2016-09-23| FB| 127.96|  | 
| 2016-09-23| AMZN| 805.75| +1.05 | 
| 2016-09-26| PCG| 63.90| -0.30 | 
| 2016-09-26| AAPL| 112.954| +0.244 | 
| 2016-09-26| AMC| 30.63| -0.70 | 
| 2016-09-26| NFLX| 94.56| -1.38 | 
| 2016-09-26| WMT| 71.62| -0.73 | 
| 2016-09-26| FDX| 175.42| +1.03 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

