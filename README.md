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
| 2016-10-10| COST| 150.28| +0.29 | 
| 2016-10-10| ATVI| 43.865| -0.055 | 
| 2016-10-10| MSFT| 58.315| +0.515 | 
| 2016-10-10| GE| 28.905| -0.175 | 
| 2016-10-10| BA| 135.84| +1.99 | 
| 2016-10-10| AMD| 6.84| +0.09 | 
| 2016-10-10| UPS| 109.05| +0.25 | 
| 2016-10-10| FB| 130.44| +1.45 | 
| 2016-10-10| AMZN| 843.61| +4.18 | 
| 2016-10-10| PCG| 59.26| -0.06 | 
| 2016-10-10| AAPL| 116.232| +2.172 | 
| 2016-10-10| AMC| 32.30| +0.06 | 
| 2016-10-10| NFLX| 103.33| -1.49 | 
| 2016-10-10| WMT| 68.006| -0.694 | 
| 2016-10-10| FDX| 174.21| +1.20 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

