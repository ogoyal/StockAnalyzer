# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-12| COST| 152.04| +0.93| +0.62% | 
| 2017-07-11| ATVI| 57.98| -0.53| -0.91% | 
| 2017-07-11| MSFT| 69.99| +0.01| +0.01% | 
| 2017-07-11| GE| 26.39| +0.35| +1.34% | 
| 2017-07-11| BA| 206.27| +2.31| +1.13% | 
| 2017-07-11| AMD| 13.89| +0.08| +0.58% | 
| 2017-07-11| BOX| 18.29| +0.24| +1.33% | 
| 2017-07-11| FB| 155.30| +1.80| +1.17% | 
| 2017-07-11| AMZN| 993.65| -2.82| -0.28% | 
| 2017-07-12| PCG| 65.57| +0.52| +0.80% | 
| 2017-07-11| AAPL| 145.57| +0.51| +0.35% | 
| 2017-07-11| AMC| 22.30| +0.80| +3.72% | 
| 2017-07-12| P| 9.205| +0.115| +1.265% | 
| 2017-07-11| WMT| 73.47| +0.24| +0.33% | 
| 2017-07-12| FDX| 217.95| +0.41| +0.19% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

