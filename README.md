# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-17| COST| 152.84| -0.16| -0.10% | 
| 2017-07-17| ATVI| 60.50| -0.25| -0.41% | 
| 2017-07-17| MSFT| 73.35| +0.57| +0.78% | 
| 2017-07-17| GE| 26.82| +0.04| +0.15% | 
| 2017-07-17| BA| 209.00| +0.49| +0.24% | 
| 2017-07-17| AMD| 13.80| -0.12| -0.86% | 
| 2017-07-17| BOX| 19.02| +0.15| +0.79% | 
| 2017-07-17| FB| 159.73| -0.24| -0.15% | 
| 2017-07-17| AMZN| 1010.04| +8.23| +0.82% | 
| 2017-07-17| PCG| 66.48| +0.13| +0.20% | 
| 2017-07-17| AAPL| 149.56| +0.52| +0.35% | 
| 2017-07-17| AMC| 19.70| -2.20| -10.05% | 
| 2017-07-17| P| 9.44| +0.19| +2.05% | 
| 2017-07-17| WMT| 76.37| +0.03| +0.04% | 
| 2017-07-18| FDX| 212.72| -2.76| -1.28% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

