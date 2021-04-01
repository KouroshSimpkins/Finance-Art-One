"""Uses yfinance to grab the lowest, close and highest price of a given ticker for a certain length of time"""

import yfinance as yf

def get_prices(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    high = str(todays_data['High'][0])
    low = str(todays_data['Low'][0])
    close = str(todays_data['Close'][0])
    three_vals = 'high = ' + high + ', low = ' + low + ', close = ' + close
    return three_vals

