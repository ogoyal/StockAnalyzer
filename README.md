# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-08-03| COST| 157.3865| -3.8935| -2.4141% | 
| 2017-08-04| ATVI| 62.47| -1.50| -2.34% | 
| 2017-08-03| MSFT| 72.15| -0.11| -0.15% | 
| 2017-08-03| GE| 25.76| +0.24| +0.94% | 
| 2017-08-03| BA| 238.25| +0.30| +0.13% | 
| 2017-08-03| AMD| 13.24| -0.13| -0.97% | 
| 2017-08-04| BOX| 18.81| +0.07| +0.37% | 
| 2017-08-03| FB| 168.59| -0.71| -0.42% | 
| 2017-08-03| AMZN| 986.92| -8.97| -0.90% | 
| 2017-08-03| PCG| 68.91| +0.52| +0.76% | 
| 2017-08-03| AAPL| 155.57| -1.57| -1.00% | 
| 2017-08-03| AMC| 15.10| -0.10| -0.66% | 
| 2017-08-03| P| 8.37| -0.01| -0.12% | 
| 2017-08-03| WMT| 80.87| +0.34| +0.42% | 
| 2017-08-03| FDX| 209.36| -0.14| -0.07% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

