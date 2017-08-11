# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-11| COST| 157.54 | 
| 2017-08-11| ATVI| 60.65 | 
| 2017-08-11| MSFT| 71.88 | 
| 2017-08-11| GE| 25.31 | 
| 2017-08-11| BA| 233.97 | 
| 2017-08-11| AMD| 12.13 | 
| 2017-08-11| BOX| 18.27 | 
| 2017-08-11| FB| 168.14 | 
| 2017-08-11| AMZN| 966.57 | 
| 2017-08-11| PCG| 69.33 | 
| 2017-08-11| AAPL| 157.44 | 
| 2017-08-11| AMC| 14.18 | 
| 2017-08-11| P| 8.11 | 
| 2017-08-11| WMT| 80.85 | 
| 2017-08-11| FDX| 206.17 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

