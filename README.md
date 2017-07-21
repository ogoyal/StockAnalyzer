# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-20| COST| 150.99| -0.25| -0.17% | 
| 2017-07-20| ATVI| 61.08| -0.25| -0.41% | 
| 2017-07-20| MSFT| 74.22| +0.36| +0.49% | 
| 2017-07-20| GE| 26.69| -0.25| -0.93% | 
| 2017-07-20| BA| 210.28| -0.60| -0.28% | 
| 2017-07-20| AMD| 13.80| +0.25| +1.85% | 
| 2017-07-20| BOX| 19.83| -0.02| -0.10% | 
| 2017-07-20| FB| 164.53| +0.39| +0.24% | 
| 2017-07-20| AMZN| 1028.70| +1.83| +0.18% | 
| 2017-07-20| PCG| 67.64| +0.54| +0.80% | 
| 2017-07-20| AAPL| 150.34| -0.68| -0.45% | 
| 2017-07-20| AMC| 20.65| +0.80| +4.03% | 
| 2017-07-20| P| 9.40| -0.04| -0.42% | 
| 2017-07-20| WMT| 76.02| +0.15| +0.20% | 
| 2017-07-20| FDX| 211.88| -1.00| -0.47% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

