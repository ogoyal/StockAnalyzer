# Stock Analyzer [![Build Status](https://travis-ci.org/ogoyal/StockAnalyzer.svg?branch=master)](https://travis-ci.org/ogoyal/StockAnalyzer)

### Run make
```
make
```

Runs python program to produce a stock data csv file. Program uses google finance api to pull stock info.

Today's data:

| Date| Stocks| Price($) | 
| --- | --- | ---  | 
| 2017-08-31| COST| 155.75 | 
| 2017-08-31| ATVI| 65.73 | 
| 2017-08-31| MSFT| 74.55 | 
| 2017-08-31| GE| 24.52 | 
| 2017-08-31| BA| 239.33 | 
| 2017-08-31| AMD| 13.01 | 
| 2017-08-31| BOX| 19.47 | 
| 2017-08-31| FB| 170.87 | 
| 2017-08-31| AMZN| 977.76 | 
| 2017-08-31| PCG| 70.32 | 
| 2017-08-31| AAPL| 163.63 | 
| 2017-08-31| AMC| 13.43 | 
| 2017-08-31| P| 8.33 | 
| 2017-08-31| WMT| 78.49 | 
| 2017-08-31| FDX| 213.81 | 

### Build/Run project

Program will monitor stocks daily. Append your list of stocks in tickers.txt

### APIs
googlefinance 0.7 : Python module to get stock data from Google Finance

```
pip install googlefinance
```

