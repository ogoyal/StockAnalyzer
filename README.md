# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-27| COST| 152.36| +0.27| +0.18% | 
| 2017-07-27| ATVI| 62.60| -0.04| -0.06% | 
| 2017-07-26| MSFT| 74.05| -0.14| -0.19% | 
| 2017-07-26| GE| 25.59| +0.15| +0.59% | 
| 2017-07-26| BA| 233.45| +20.99| +9.88% | 
| 2017-07-26| AMD| 14.76| +0.65| +4.61% | 
| 2017-07-26| BOX| 19.92| +0.03| +0.15% | 
| 2017-07-26| FB| 165.61| +0.33| +0.20% | 
| 2017-07-26| AMZN| 1052.80| +12.93| +1.24% | 
| 2017-07-26| PCG| 67.90| +0.39| +0.58% | 
| 2017-07-26| AAPL| 153.46| +0.72| +0.47% | 
| 2017-07-26| AMC| 21.05| |  | 
| 2017-07-26| P| 9.75| -0.08| -0.81% | 
| 2017-07-26| WMT| 78.90| +0.38| +0.48% | 
| 2017-07-26| FDX| 213.63| -0.74| -0.35% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

