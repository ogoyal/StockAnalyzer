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
| 2016-10-26| COST| 49.865| +0.275 | 
| 2016-10-26| ATVI| 43.37| -0.14 | 
| 2016-10-26| MSFT| 35.975| +0.045 | 
| 2016-10-26| GE| 24.01| +0.24 | 
| 2016-10-26| BA| 39.69| +0.23 | 
| 2016-10-26| AMD| 43.55| +0.04 | 
| ---| UPS| |  | 
| 2016-10-26| FB| 11.845| -0.005 | 
| 2016-10-26| AMZN| 43.37| -0.14 | 
| 2016-10-26| PCG| 11.77| -0.41 | 
| 2016-10-26| AAPL| 43.55| +0.04 | 
| 2016-10-26| AMC| 43.56| +0.05 | 
| 2016-10-26| NFLX| 100.56| -0.19 | 
| 2016-10-26| WMT| 34.53| -0.71 | 
| 2016-10-26| FDX| 11.845| -0.005 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

