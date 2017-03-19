import requests
import re


def get_sentiment_average(text_array):
    company_scores = {}
    for key in text_array:
        company_scores[key] = get_sentiment_score(text_array[key])
    return company_scores


def get_sentiment_score(messages):
    # data = str(messages)
    # the below string is an edited version of messages, but as a string.  This still fails on the API call...
    data = "{'data':[{'text':'Exxon says a technical glitch means some Tillerson alias emails may be lost  '},{'text': u'Sec\'y of State Tillerson while at Exxon would use email alias Wayne Tracker to discuss climate change, per NY AG\n\n'},{'text': u'He has probably never worked this hard in his entire life. Imagine his shock and depression as he realizes he could\u2026 '}]}"
    base_sentiment_url = "http://www.sentiment140.com/api/bulkClassifyJson"
    r = requests.post(base_sentiment_url, data=data)
    sum = 0
    count = 0
    for entry in r.json()['data']:
        sum = sum + entry['polarity']
        count += 1
    return sum/count

