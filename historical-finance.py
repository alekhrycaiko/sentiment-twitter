from yahoo_finance import Share
facebook = Share('FB')
print(facebook.get_historical('2012-04-25', '2015-03-10'))