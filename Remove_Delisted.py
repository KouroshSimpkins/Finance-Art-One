"""should use yfinance to remove any delisted tickers from the Stock_Prices.txt file"""

import yfinance as yf

tickers = []
removing_tickers = []

