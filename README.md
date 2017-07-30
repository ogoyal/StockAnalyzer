# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-28| COST| 152.89| +0.37| +0.24% | 
| 2017-07-28| ATVI| 61.45| +0.28| +0.46% | 
| 2017-07-28| MSFT| 73.04| -0.12| -0.16% | 
| 2017-07-28| GE| 25.53| -0.26| -1.01% | 
| 2017-07-28| BA| 241.27| +0.27| +0.11% | 
| 2017-07-28| AMD| 13.95| -0.17| -1.20% | 
| 2017-07-28| BOX| 19.24| -0.21| -1.08% | 
| 2017-07-28| FB| 172.45| +2.01| +1.18% | 
| 2017-07-28| AMZN| 1020.04| -25.96| -2.48% | 
| 2017-07-28| PCG| 67.45| -0.10| -0.15% | 
| 2017-07-28| AAPL| 149.50| -1.06| -0.70% | 
| 2017-07-28| AMC| 20.50| -0.20| -0.97% | 
| 2017-07-28| P| 9.47| -0.18| -1.87% | 
| 2017-07-28| WMT| 79.81| +0.03| +0.04% | 
| 2017-07-28| FDX| 208.04| +0.50| +0.24% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

