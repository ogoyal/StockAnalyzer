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
| 2017-07-07| COST| 157.29| +0.20| +0.13% | 
| 2017-07-06| ATVI| 56.62| -0.54| -0.94% | 
| 2017-07-06| MSFT| 68.57| -0.51| -0.74% | 
| 2017-07-06| GE| 26.31| -1.04| -3.80% | 
| 2017-07-06| BA| 201.48| -0.33| -0.16% | 
| 2017-07-06| AMD| 13.02| -0.17| -1.29% | 
| 2017-07-07| BOX| 17.845| +0.075| +0.422% | 
| 2017-07-06| FB| 148.82| -1.52| -1.01% | 
| 2017-07-06| AMZN| 965.14| -6.26| -0.64% | 
| 2017-07-07| PCG| 65.48| +0.27| +0.41% | 
| 2017-07-06| AAPL| 142.73| -1.36| -0.94% | 
| 2017-07-07| AMC| 21.70| +0.05| +0.23% | 
| 2017-07-07| P| 8.535| -0.105| -1.215% | 
| 2017-07-06| WMT| 75.47| +0.15| +0.20% | 
| 2017-07-07| FDX| 217.63| +2.60| +1.21% | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.4.0 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

