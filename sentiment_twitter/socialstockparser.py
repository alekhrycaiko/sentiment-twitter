import time
import datetime as DT
import tweepy
import re
import HTMLParser
import schedule
from datetime import date
from sentiment_twitter import sentiment_api

consumer_key = '4pAS5n5wiqrLUotVFGcgAbQ9g'
consumer_secret = 'FxWIFR8c1Dk4D64ZJqo0pls5LPp9664wzbvJJz2LyYyifxP4Dn'
access_token = '2479204615-f69dFnvC7HRs9PLpTMGxAIVTpHgUUkAJv8dRHgY'
access_secret = '9cFQIBGSjVNPOK2UAlleQMJi8ol76T1ViN2NROc4dhGxC'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
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
                tweet = public_tweets.next()
                # Insert into db - potential for large data set for historical analysis
                for tweet in public_tweets:
                    t = tweet.text
                    text = re.sub(r"http\S+", "", t)
                    text = html_parser.unescape(text)
                    text = re.sub('[^A-Za-z0-9]+', ' ', text)
                    tweets.append(text)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                continue
            except StopIteration:
                break
    print data
    return data


def extract_company_tweets(dictionary):
    total = {}
    for key in dictionary:
        company = {}
        tweets = []
        for text in dictionary[key]:
            tweets.append({"text": text})
        company["data"] = tweets
        total[key] = company
    print total
    return total


def company_sentiments():
    # change list of companies and count to 1000
    d = ["apple", "facebook", "exxon", "nvidia", "netflix", "adobe"]
    q = tweetText(d, 5, date.today() - DT.timedelta(days=7), date.today())

    schedule.every(3).days.at("01:00").do(tweetText(d, 5000, date.today() - DT.timedelta(days=3), date.today()))

    ret = {}
    for key in q:
        sentiment = sentiment_api.get_sentiment_average(extract_company_tweets(q))
        ret[key] = sentiment
    return ret

print company_sentiments()

# while True:
#     schedule.run_pending()
#     time.sleep(1)
