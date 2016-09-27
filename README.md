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
| 2016-09-26| COST| 151.19| -1.34 | 
| 2016-09-26| ATVI| 43.98| -0.38 | 
| 2016-09-23| MSFT| 57.43| -0.39 | 
| 2016-09-26| GE| 29.54| -0.35 | 
| 2016-09-26| BA| 130.57| -1.21 | 
| 2016-09-26| AMD| 6.375| -0.175 | 
| 2016-09-26| UPS| 108.84| -0.37 | 
| 2016-09-23| FB| 127.96| -2.12 | 
| 2016-09-26| AMZN| 800.1764| -5.5736 | 
| 2016-09-23| PCG| 64.20| +0.18 | 
| 2016-09-26| AAPL| 112.93| +0.22 | 
| 2016-09-23| AMC| 31.33|  | 
| 2016-09-26| NFLX| 94.34| -1.60 | 
| 2016-09-26| WMT| 71.62| -0.73 | 
| 2016-09-26| FDX| 175.34| +0.95 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

