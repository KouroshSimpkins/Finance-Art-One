"""Uses yfinance to grab the lowest, close and highest price of a given ticker for a certain length of time"""

import yfinance as yf

tickers = []

def get_prices(symbol):
    ticker = yf.Ticker(symbol)
    delisted = False

    try:
        todays_data = ticker.history(period='1d')
        high = str(todays_data['High'][0])
        low = str(todays_data['Low'][0])
        close = str(todays_data['Close'][0])
# who wrote this garbage pile of data tunneling?! Oh I did...
    except IndexError: #If there is an index error then the chances are that the symbol has been delisted for whatever reason. 
        delisted = True
        return delisted
    
    except:
        high = 'n/a'
        low = 'n/a'
        close = 'n/a'

    finally:
        if delisted:
            return delisted
        three_vals = {'high':high, 'low':low , 'close':close}
        return three_vals

def store_prices():
    with open('Stocks_List.txt', mode='r+') as f:
        with open('Stock_Prices.txt', mode='w') as w:
            for ticker in f:
                temp = {ticker.strip(): get_prices(str(ticker.strip()))}
                w.write(str(temp))
                w.write('\n')

store_prices()
