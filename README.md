# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-10| COST| 151.99| -2.12| -1.38% | 
| 2017-07-07| ATVI| 58.09| |  | 
| 2017-07-07| MSFT| 69.46| +0.89| +1.30% | 
| 2017-07-07| GE| 26.15| -0.16| -0.61% | 
| 2017-07-07| BA| 202.37| +0.89| +0.44% | 
| 2017-07-07| AMD| 13.36| +0.34| +2.61% | 
| 2017-07-07| BOX| 18.19| +0.42| +2.36% | 
| 2017-07-07| FB| 151.44| +2.62| +1.76% | 
| 2017-07-07| AMZN| 978.76| +13.62| +1.41% | 
| 2017-07-07| PCG| 65.32| +0.11| +0.17% | 
| 2017-07-07| AAPL| 144.18| +1.45| +1.02% | 
| 2017-07-07| AMC| 21.95| +0.30| +1.39% | 
| 2017-07-07| P| 8.51| -0.13| -1.50% | 
| 2017-07-07| WMT| 75.33| -0.14| -0.19% | 
| 2017-07-07| FDX| 218.51| +3.48| +1.62% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

