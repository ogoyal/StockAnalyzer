# CSVTableContainer
C++ Program using Standard Library

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses yahoo-finance api to pull stock info.
Creates a C++ program to do data analytics.

Sample CSV data file:

| Date| Stocks| Price($)| Change($) | 
| --- | --- | --- | ---  | 
| 2016-10-18| COST| 48.99| +0.39 | 
| 2016-10-18| ATVI| 45.44| +0.29 | 
| 2016-10-18| MSFT| 35.20| +0.11 | 
| 2016-10-18| GE| 23.65| +0.13 | 
| 2016-10-18| BA| 39.22| +0.35 | 
| 2016-10-18| AMD| 45.44| +0.29 | 
| ---| UPS| |  | 
| 2016-10-18| FB| 11.89| +0.01 | 
| 2016-10-18| AMZN| 45.44| +0.29 | 
| 2016-10-18| PCG| 12.50| +0.12 | 
| 2016-10-18| AAPL| 45.44| +0.29 | 
| 2016-10-18| AMC| 45.44| +0.29 | 
| 2016-10-18| NFLX| 100.49| -0.03 | 
| 2016-10-18| WMT| 36.42| +0.69 | 
| 2016-10-18| FDX| 11.89| +0.01 | 

### Build/Run project
```
source StockAnalyzer/bin/activate
pip3 install -r requirements.txt
#TODO Setup django environment - postgresql
python3 manage.py runserver 0.0.0.0:8000
```

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
yahoo-finance 1.1.4 : Python module to get stock data from Yahoo! Finance

```
pip install yahoo-finance
```

