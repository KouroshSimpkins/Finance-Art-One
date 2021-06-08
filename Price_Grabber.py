"""Uses yfinance to grab the lowest, close and highest price of a given ticker for a certain length of time"""

import yfinance as yf
import csv

tickers = []

def get_prices(symbol):
    ticker = yf.Ticker(symbol)
    delisted = False
    isup = False

    try:
        todays_data = ticker.history(period='1d')
        high = str(todays_data['High'][0])
        low = str(todays_data['Low'][0])
        close = str(todays_data['Close'][0])
        Open = str(todays_data['Open'][0])
        if close > Open:
            isup = True
        elif close < Open:
            isup = False
        

    except IndexError: #If there is an index error then the chances are that the symbol has been delisted for whatever reason. 
        delisted = True
        return delisted
    
    except:
        high = 'n/a'
        low = 'n/a'
        close = 'n/a'
        Open = 'n/a'

    finally:
        if delisted:
            return delisted
        # three_vals = {'high':high, 'low':low , 'close':close}
        # three_vals is ignored now because we can return the data directly as a tuple
        # keeping it here for the moment but don't really need it.
        return Open,high,low,close,isup



def store_prices():
    """deprecated, use store_prices_csv"""
    with open('Stocks_List.txt', mode='r+') as f:
        with open('Stock_Prices.txt', mode='w') as w:
            for ticker in f:
                temp = {ticker.strip(): get_prices(str(ticker.strip()))}
                w.write(str(temp))
                w.write('\n')

def delisted_tickers():
    #TODO #3
    with open('Stocks_List.txt', mode='r+') as f:
        with open('Delisted_Stocks.txt', mode='w') as w:
            for ticker in f:
                temp = {ticker.strip(): get_prices(str(ticker.strip()))}
                if temp:
                    w.write(str(temp))
                    w.write('\n')
                else:
                    pass

def store_prices_csv():
    with open('Stocks_List.txt', mode='r+') as f:
        with open('Stock_Prices.csv', mode='w', newline='') as w:
            writer = csv.writer(w)
            writer.writerow(["SN", "Ticker", "Open", "High", "Low", "Close", "isup"])
            i = 0
            for ticker in f:
                try:
                    Open, High, Low, Close, isup = get_prices(str(ticker.strip()))
                    if Open != 'n/a':
                        writer.writerow([i, str(ticker.strip()), Open, High, Low, Close, isup])
                        i += 1
                    elif Open == 'n/a':
                        print(ticker.strip(), "has no data to write")
                        pass
                except TypeError:
                    pass

store_prices_csv()