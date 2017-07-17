# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-14| COST| 153.00| -0.60| -0.39% | 
| 2017-07-14| ATVI| 60.75| +0.25| +0.41% | 
| 2017-07-14| MSFT| 72.78| +1.01| +1.41% | 
| 2017-07-14| GE| 26.78| -0.01| -0.04% | 
| 2017-07-14| BA| 208.51| +2.28| +1.11% | 
| 2017-07-14| AMD| 13.92| +0.39| +2.88% | 
| 2017-07-14| BOX| 18.87| +0.06| +0.32% | 
| 2017-07-14| FB| 159.97| +0.71| +0.45% | 
| 2017-07-14| AMZN| 1001.81| +1.18| +0.12% | 
| 2017-07-14| PCG| 66.35| +0.15| +0.23% | 
| 2017-07-14| AAPL| 149.04| +1.27| +0.86% | 
| 2017-07-14| AMC| 21.90| -0.25| -1.13% | 
| 2017-07-14| P| 9.24| +0.07| +0.82% | 
| 2017-07-14| WMT| 76.34| +1.29| +1.72% | 
| 2017-07-14| FDX| 219.06| +1.09| +0.50% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

