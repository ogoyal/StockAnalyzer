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
| 2017-06-30| COST| 159.93|  | 
| 2017-06-30| ATVI| 57.57| -0.01 | 
| 2017-06-30| MSFT| 68.93| +0.44 | 
| 2017-06-30| GE| 27.01| -0.01 | 
| 2017-06-30| BA| 197.75| +0.29 | 
| 2017-06-30| AMD| 12.48| -0.12 | 
| 2017-06-30| BOX| 18.24| +0.18 | 
| 2017-06-30| FB| 150.98| -0.06 | 
| 2017-06-30| AMZN| 968.00| -7.93 | 
| 2017-07-03| PCG| 66.03| -0.34 | 
| 2017-06-30| AAPL| 144.02| +0.34 | 
| 2017-07-03| AMC| 23.20| +0.45 | 
| 2017-06-30| P| 8.92| -0.23 | 
| 2017-06-30| WMT| 75.68| -0.25 | 
| 2017-07-03| FDX| 218.23| +0.90 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

