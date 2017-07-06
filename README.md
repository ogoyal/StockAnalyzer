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
| 2017-07-05| COST| 158.94| +0.12| +0.08% | 
| 2017-07-03| ATVI| 56.26| -1.31| -2.28% | 
| 2017-07-03| MSFT| 68.17| -0.76| -1.10% | 
| 2017-07-03| GE| 27.45| +0.44| +1.63% | 
| 2017-07-03| BA| 198.59| +0.84| +0.42% | 
| 2017-07-03| AMD| 12.15| -0.33| -2.64% | 
| 2017-07-03| BOX| 18.08| -0.16| -0.88% | 
| 2017-07-03| FB| 148.43| -2.55| -1.69% | 
| 2017-07-03| AMZN| 953.66| -14.34| -1.48% | 
| 2017-07-05| PCG| 65.28| -0.34| -0.52% | 
| 2017-07-03| AAPL| 143.50| -0.52| -0.36% | 
| 2017-07-05| AMC| 22.75| -0.45| -1.94% | 
| 2017-07-03| P| 8.77| -0.15| -1.68% | 
| 2017-07-03| WMT| 75.36| -0.32| -0.42% | 
| 2017-07-05| FDX| 219.14| +1.76| +0.81% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

