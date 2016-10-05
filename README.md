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
| 2016-10-04| COST| 150.48| -0.53 | 
| 2016-10-04| ATVI| 43.91| -0.19 | 
| 2016-10-04| MSFT| 57.31| -0.11 | 
| 2016-10-04| GE| 29.50| -0.14 | 
| 2016-10-04| BA| 132.25| -0.13 | 
| 2016-10-04| AMD| 6.99| +0.04 | 
| 2016-10-04| UPS| 108.80| -0.38 | 
| 2016-10-04| FB| 128.19| -0.58 | 
| 2016-10-04| AMZN| 833.1627| -3.5773 | 
| 2016-10-04| PCG| 58.89| -1.27 | 
| 2016-10-04| AAPL| 112.87| +0.35 | 
| 2016-10-04| AMC| 31.63| -0.59 | 
| 2016-10-04| NFLX| 102.34| -0.29 | 
| 2016-10-04| WMT| 71.75| -0.26 | 
| 2016-10-04| FDX| 173.60| -0.70 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

