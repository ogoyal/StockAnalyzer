# Stock Analyzer

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.

Sample data:

| Date| Stocks| Price($)| Change($)| Change(%) | 
| --- | --- | --- | --- | ---  | 
| 2017-07-28| COST| 152.25| -0.27| -0.18% | 
| 2017-07-28| ATVI| 60.9499| -0.2201| -0.3598% | 
| 2017-07-27| MSFT| 73.16| -0.89| -1.20% | 
| 2017-07-28| GE| 25.53| -0.26| -1.01% | 
| 2017-07-27| BA| 241.00| +7.55| +3.23% | 
| 2017-07-27| AMD| 14.12| -0.64| -4.34% | 
| 2017-07-27| BOX| 19.45| -0.47| -2.36% | 
| 2017-07-27| FB| 170.44| +4.83| +2.92% | 
| 2017-07-27| AMZN| 1046.00| -6.80| -0.65% | 
| 2017-07-27| PCG| 67.55| -0.35| -0.52% | 
| 2017-07-27| AAPL| 150.56| -2.90| -1.89% | 
| 2017-07-27| AMC| 20.70| -0.35| -1.66% | 
| 2017-07-28| P| 9.47| -0.18| -1.87% | 
| 2017-07-27| WMT| 79.78| +0.88| +1.12% | 
| 2017-07-28| FDX| 208.13| +0.59| +0.28% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

