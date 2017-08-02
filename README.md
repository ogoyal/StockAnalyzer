# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-08-01| COST| 159.719| +1.209| +0.763% | 
| 2017-08-01| ATVI| 62.15| +0.37| +0.60% | 
| 2017-07-31| MSFT| 72.70| -0.34| -0.47% | 
| 2017-07-31| GE| 25.61| +0.08| +0.31% | 
| 2017-07-31| BA| 242.46| +1.19| +0.49% | 
| 2017-07-31| AMD| 13.61| -0.34| -2.44% | 
| 2017-07-31| BOX| 18.85| -0.39| -2.03% | 
| 2017-07-31| FB| 169.25| -3.20| -1.86% | 
| 2017-07-31| AMZN| 987.78| -32.26| -3.16% | 
| 2017-07-31| PCG| 67.69| +0.24| +0.36% | 
| 2017-07-31| AAPL| 148.73| -0.77| -0.52% | 
| 2017-08-01| AMC| 20.7858| +0.3858| +1.8912% | 
| 2017-08-01| P| 8.505| -0.445| -4.972% | 
| 2017-07-31| WMT| 79.99| +0.18| +0.23% | 
| 2017-08-01| FDX| 206.3062| -1.7238| -0.8286% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

