# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-24| COST| 150.71| +0.27| +0.18% | 
| 2017-07-21| ATVI| 60.93| -0.15| -0.25% | 
| 2017-07-21| MSFT| 73.79| -0.43| -0.58% | 
| 2017-07-21| GE| 25.91| -0.78| -2.92% | 
| 2017-07-21| BA| 212.14| +1.86| +0.88% | 
| 2017-07-21| AMD| 13.88| +0.08| +0.58% | 
| 2017-07-24| BOX| 19.69| +0.01| +0.05% | 
| 2017-07-21| FB| 164.43| -0.10| -0.06% | 
| 2017-07-21| AMZN| 1025.67| -3.03| -0.29% | 
| 2017-07-21| PCG| 68.26| +0.62| +0.92% | 
| 2017-07-21| AAPL| 150.27| -0.07| -0.05% | 
| 2017-07-21| AMC| 20.35| -0.25| -1.21% | 
| 2017-07-21| P| 9.47| +0.33| +3.61% | 
| 2017-07-21| WMT| 76.15| +0.13| +0.17% | 
| 2017-07-24| FDX| 212.8767| +0.3667| +0.1726% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

