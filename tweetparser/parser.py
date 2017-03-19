import time

import datetime as DT
import tweepy
import re
import HTMLParser
import schedule
from datetime import date

consumer_key = 'AX99l75lGAiEXKewGv6UbjnzP'
consumer_secret = 'UJtQXT02ieWvAEPy3kk7iqYMkL6Vom7zfIdTJZlyvMkSqegvPw'
access_token = '727254860375052289-dImeSLNMLOs4pDxnqypV3hytZL4rF49'
access_secret = 'khWVlagGWmJ6S5F3rjt9wLJDTXBzZm4Hr4TqRdbzMwcIQ'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
html_parser = HTMLParser.HTMLParser()


def tweetText(d, count, since, until):

    data = {}

    for company in d:
        tweets = []
        public_tweets = tweepy.Cursor(api.search,
                           q=company, include_entities=False, lang="en", since=since, until=until).items(count)
        data[company] = tweets

        while True:
            try:
                # Insert into db - potential for large data set for historical analysis
                for tweet in public_tweets:
                    t = tweet.text
                    text = re.sub(r"http\S+", "", t)
                    text = html_parser.unescape(text)
                    tweets.append(text)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                continue
            except StopIteration:
                break

    print data
    return data

# change list of companies and count to 1000
d = ["apple", "facebook", "exxon", "nvidia", "netflix", "adobe"]
tweetText(d, 5, date.today()-DT.timedelta(days=7), date.today())

schedule.every(3).days.at("01:00").do(tweetText(d, 5000, date.today()-DT.timedelta(days=3), date.today()))

# save to db?

while True:
    schedule.run_pending()
    time.sleep(1)
