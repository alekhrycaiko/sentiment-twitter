import schedule
from scipy.stats.stats import pearsonr
from socialstockparser import tweetText
from PriceFetcher import getThreeYearClosingPrices
from datetime import date
import datetime as DT
import time

d = ["apple", "facebook", "exxon", "nvidia", "netflix", "adobe"]
ticker = ['AAPL', 'FB', 'XOM', 'NVDA', 'NFLX', 'ADBE']

# tweetText(d, 5, date.today()-DT.timedelta(days=7), date.today())
a = [3,4,5,6]
b = getThreeYearClosingPrices(ticker, 2)
c = []

for key in b:
    c.append(b[key])
print "ss"
print c

# print pearsonr(a,b)

