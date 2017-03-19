from yahoo_finance import Share
import datetime
from dateutil.relativedelta import relativedelta

"""
Call with a ticket symbol to get an array of closing prices for the last three years, relative to the date which the
function is called.  The returned array consists of pricepoint tuples, which can be accessed with .date and .price
fields
"""


def getThreeYearClosingPrices(ticker, days):
    prices = {}
    for t in ticker:
        facebook = Share(t)
        data = facebook.get_historical((datetime.datetime.now() - relativedelta(days=days)).strftime("%Y-%m-%d"),
                                       datetime.datetime.now().strftime("%Y-%m-%d"))
        price_data = []
        prices[t] = price_data

        for day in data:
            price_data.append(round(float(day['Close']), 2))

        price_data.reverse()
    # print prices
    return prices

ticker = ['AAPL', 'FB', 'XOM', 'NVDA', 'NFLX', 'ADBE']

#print(getThreeYearClosingPrices(ticker, 5))



