# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-12| COST| 151.75| +0.64| +0.42% | 
| 2017-07-12| ATVI| 61.02| +3.04| +5.24% | 
| 2017-07-12| MSFT| 71.15| +1.16| +1.66% | 
| 2017-07-12| GE| 26.58| +0.20| +0.76% | 
| 2017-07-12| BA| 206.44| +0.17| +0.08% | 
| 2017-07-12| AMD| 14.29| +0.40| +2.88% | 
| 2017-07-12| BOX| 18.67| +0.38| +2.08% | 
| 2017-07-12| FB| 158.90| +3.63| +2.34% | 
| 2017-07-12| AMZN| 1006.51| +12.38| +1.25% | 
| 2017-07-12| PCG| 65.04| -0.01| -0.02% | 
| 2017-07-12| AAPL| 145.74| +0.21| +0.14% | 
| 2017-07-12| AMC| 21.40| -0.90| -4.04% | 
| 2017-07-12| P| 9.16| +0.07| +0.77% | 
| 2017-07-12| WMT| 73.94| +0.47| +0.64% | 
| 2017-07-12| FDX| 218.32| +0.78| +0.36% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

