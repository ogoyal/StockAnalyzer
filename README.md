# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-16| COST| 159.76 | 
| 2017-08-16| ATVI| 62.89 | 
| 2017-08-16| MSFT| 73.65 | 
| 2017-08-16| GE| 25.10 | 
| 2017-08-16| BA| 237.59 | 
| 2017-08-16| AMD| 12.63 | 
| 2017-08-16| BOX| 18.84 | 
| 2017-08-16| FB| 170.00 | 
| 2017-08-16| AMZN| 978.18 | 
| 2017-08-16| PCG| 69.56 | 
| 2017-08-16| AAPL| 160.95 | 
| 2017-08-16| AMC| 13.30 | 
| 2017-08-16| P| 8.67 | 
| 2017-08-16| WMT| 80.98 | 
| 2017-08-16| FDX| 209.63 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

