from yahoo_finance import Share
import datetime
from dateutil.relativedelta import relativedelta

"""
Call with a ticket symbol to get an array of closing prices for the last three years, relative to the date which the
function is called.  The returned array consists of pricepoint tuples, which can be accessed with .date and .price
fields
"""
def getThreeYearClosingPrices(ticker):
    facebook = Share(ticker)
    data = facebook.get_historical((datetime.datetime.now() - relativedelta(years=3)).strftime("%Y-%m-%d"),
                                   datetime.datetime.now().strftime("%Y-%m-%d"))
    price_data = []

    for day in data:
        pp = {'day': day['Date'], 'price': round(float(day['Close']), 2)}
        price_data.append(pp)

    price_data.reverse()
    return price_data




