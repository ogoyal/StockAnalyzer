# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-08-03| COST| 157.86| -3.42| -2.12% | 
| 2017-08-03| ATVI| 63.12| +1.67| +2.72% | 
| 2017-08-02| MSFT| 72.26| -0.32| -0.44% | 
| 2017-08-02| GE| 25.52| +0.08| +0.31% | 
| 2017-08-02| BA| 237.95| -1.49| -0.62% | 
| 2017-08-02| AMD| 13.37| -0.34| -2.48% | 
| 2017-08-03| BOX| 18.74| -0.06| -0.32% | 
| 2017-08-02| FB| 169.30| -0.56| -0.33% | 
| 2017-08-02| AMZN| 995.89| -0.30| -0.03% | 
| 2017-08-02| PCG| 68.39| +0.17| +0.25% | 
| 2017-08-02| AAPL| 157.14| +7.09| +4.73% | 
| 2017-08-03| AMC| 15.10| -0.10| -0.66% | 
| 2017-08-03| P| 8.37| -0.01| -0.12% | 
| 2017-08-02| WMT| 80.53| +0.03| +0.04% | 
| 2017-08-03| FDX| 209.2999| -0.2001| -0.0955% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

