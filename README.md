# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-25| COST| 153.52| +2.52| +1.67% | 
| 2017-07-24| ATVI| 61.44| +0.51| +0.84% | 
| 2017-07-24| MSFT| 73.60| -0.19| -0.26% | 
| 2017-07-24| GE| 25.43| -0.48| -1.85% | 
| 2017-07-24| BA| 212.18| +0.04| +0.02% | 
| 2017-07-24| AMD| 14.16| +0.28| +2.02% | 
| 2017-07-25| BOX| 19.89| +0.20| +1.02% | 
| 2017-07-24| FB| 166.00| +1.57| +0.95% | 
| 2017-07-24| AMZN| 1038.95| +13.28| +1.29% | 
| 2017-07-24| PCG| 67.90| -0.36| -0.53% | 
| 2017-07-24| AAPL| 152.09| +1.82| +1.21% | 
| 2017-07-24| AMC| 20.50| +0.15| +0.74% | 
| 2017-07-25| P| 9.83| +0.19| +1.97% | 
| 2017-07-24| WMT| 76.89| +0.74| +0.97% | 
| 2017-07-24| FDX| 212.68| +0.17| +0.08% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

