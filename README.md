# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-18| COST| 151.50| -1.34| -0.88% | 
| 2017-07-18| ATVI| 61.33| +0.83| +1.37% | 
| 2017-07-18| MSFT| 73.30| -0.05| -0.07% | 
| 2017-07-18| GE| 26.89| +0.07| +0.26% | 
| 2017-07-18| BA| 208.24| -0.76| -0.36% | 
| 2017-07-18| AMD| 13.48| -0.32| -2.32% | 
| 2017-07-18| BOX| 19.27| +0.25| +1.31% | 
| 2017-07-18| FB| 162.86| +3.13| +1.96% | 
| 2017-07-18| AMZN| 1024.45| +14.41| +1.43% | 
| 2017-07-18| PCG| 66.63| +0.15| +0.23% | 
| 2017-07-18| AAPL| 150.08| +0.52| +0.35% | 
| 2017-07-19| AMC| 20.20| +0.10| +0.50% | 
| 2017-07-18| P| 9.56| +0.12| +1.27% | 
| 2017-07-18| WMT| 76.20| -0.17| -0.22% | 
| 2017-07-18| FDX| 212.72| -2.76| -1.28% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

