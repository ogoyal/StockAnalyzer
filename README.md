# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-08-02| COST| 161.31| +1.59| +1.00% | 
| 2017-08-02| ATVI| 60.54| -1.86| -2.98% | 
| 2017-08-01| MSFT| 72.58| -0.12| -0.17% | 
| 2017-08-01| GE| 25.44| -0.17| -0.66% | 
| 2017-08-01| BA| 239.44| -3.02| -1.25% | 
| 2017-08-01| AMD| 13.71| +0.10| +0.73% | 
| 2017-08-01| BOX| 19.01| +0.16| +0.85% | 
| 2017-08-01| FB| 169.86| +0.61| +0.36% | 
| 2017-08-01| AMZN| 996.19| +8.41| +0.85% | 
| 2017-08-01| PCG| 68.22| +0.53| +0.78% | 
| 2017-08-01| AAPL| 150.05| +1.32| +0.89% | 
| 2017-08-02| AMC| 15.90| -4.90| -23.56% | 
| 2017-08-01| P| 8.505| -0.445| -4.972% | 
| 2017-08-01| WMT| 80.50| +0.51| +0.64% | 
| 2017-08-01| FDX| 206.3062| -1.7238| -0.8286% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

