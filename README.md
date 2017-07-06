# StockAnalyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.
Creates a C++ program to do data analytics.

Sample CSV data file:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-06| COST| 159.05| +1.03| +0.65% | 
| 2017-07-05| ATVI| 57.16| +0.90| +1.60% | 
| 2017-07-05| MSFT| 69.08| +0.91| +1.33% | 
| 2017-07-05| GE| 27.35| -0.10| -0.36% | 
| 2017-07-05| BA| 201.81| +3.22| +1.62% | 
| 2017-07-05| AMD| 13.19| +1.04| +8.56% | 
| 2017-07-05| BOX| 18.11| +0.03| +0.17% | 
| 2017-07-05| FB| 150.34| +1.91| +1.29% | 
| 2017-07-05| AMZN| 971.40| +17.74| +1.86% | 
| 2017-07-06| PCG| 65.16| -0.28| -0.43% | 
| 2017-07-05| AAPL| 144.09| +0.59| +0.41% | 
| 2017-07-05| AMC| 22.45| -0.75| -3.23% | 
| 2017-07-05| P| 8.89| +0.12| +1.37% | 
| 2017-07-05| WMT| 75.32| -0.04| -0.05% | 
| 2017-07-06| FDX| 216.285| -2.025| -0.928% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

