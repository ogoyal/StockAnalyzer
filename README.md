# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-19| COST| 151.24| -0.26| -0.17% | 
| 2017-07-19| ATVI| 61.33| +0.00| +0.00% | 
| 2017-07-19| MSFT| 73.86| +0.56| +0.76% | 
| 2017-07-19| GE| 26.94| +0.05| +0.19% | 
| 2017-07-19| BA| 210.88| +2.64| +1.27% | 
| 2017-07-19| AMD| 13.55| +0.07| +0.52% | 
| 2017-07-20| BOX| 19.94| +0.09| +0.45% | 
| 2017-07-19| FB| 164.14| +1.28| +0.79% | 
| 2017-07-19| AMZN| 1026.87| +2.42| +0.24% | 
| 2017-07-19| PCG| 67.10| +0.47| +0.71% | 
| 2017-07-19| AAPL| 151.02| +0.94| +0.63% | 
| 2017-07-20| AMC| 20.425| +0.575| +2.897% | 
| 2017-07-20| P| 9.40| -0.04| -0.42% | 
| 2017-07-19| WMT| 75.87| -0.33| -0.43% | 
| 2017-07-19| FDX| 211.36| +0.32| +0.15% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

