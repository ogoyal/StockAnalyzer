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
| 2017-06-30| COST| 66.88| -0.10 | 
| 2017-06-30| ATVI| 59.31| +0.51 | 
| 2017-06-30| MSFT| 23.24| +0.29 | 
| 2017-06-30| GE| 27.83| -0.06 | 
| 2017-06-30| BA| 58.53| +0.33 | 
| 2017-06-30| AMD| 59.31| +0.51 | 
| ---| UPS| |  | 
| 2017-06-30| FB| 11.19| +0.02 | 
| 2017-06-30| AMZN| 59.31| +0.51 | 
| 2017-06-30| PCG| 8.92| -0.23 | 
| 2017-06-30| AAPL| 59.31| +0.51 | 
| 2017-06-30| AMC| 59.31| +0.51 | 
| 2016-11-04| NFLX| 90.34| +0.00 | 
| 2017-06-30| WMT| 76.88| +2.85 | 
| 2017-06-30| FDX| 11.19| +0.02 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

