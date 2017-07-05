# StockAnalyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.
Creates a C++ program to do data analytics.

Sample CSV data file:

| Date| Stocks| Price($)| Change($) | 
| --- | --- | --- | ---  | 
| 2017-07-05| COST| 158.94| +0.12 | 
| 2017-07-03| ATVI| 56.26| -1.31 | 
| 2017-07-03| MSFT| 68.17| -0.76 | 
| 2017-07-03| GE| 27.45| +0.44 | 
| 2017-07-03| BA| 198.59| +0.84 | 
| 2017-07-03| AMD| 12.15| -0.33 | 
| 2017-07-03| BOX| 18.08| -0.16 | 
| 2017-07-03| FB| 148.43| -2.55 | 
| 2017-07-03| AMZN| 953.66| -14.34 | 
| 2017-07-05| PCG| 65.28| -0.34 | 
| 2017-07-03| AAPL| 143.50| -0.52 | 
| 2017-07-05| AMC| 22.75| -0.45 | 
| 2017-07-03| P| 8.77| -0.15 | 
| 2017-07-03| WMT| 75.36| -0.32 | 
| 2017-07-05| FDX| 218.6299| +1.2499 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

