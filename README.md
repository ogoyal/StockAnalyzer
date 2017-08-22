# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-22| COST| 158.68 | 
| 2017-08-22| ATVI| 63.88 | 
| 2017-08-22| MSFT| 73.00 | 
| 2017-08-22| GE| 24.58 | 
| 2017-08-22| BA| 239.21 | 
| 2017-08-22| AMD| 12.16 | 
| 2017-08-22| BOX| 19.33 | 
| 2017-08-22| FB| 169.17 | 
| 2017-08-22| AMZN| 966.31 | 
| 2017-08-22| PCG| 69.53 | 
| 2017-08-22| AAPL| 159.64 | 
| 2017-08-22| AMC| 12.65 | 
| 2017-08-22| P| 8.48 | 
| 2017-08-22| WMT| 80.00 | 
| 2017-08-22| FDX| 208.85 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

