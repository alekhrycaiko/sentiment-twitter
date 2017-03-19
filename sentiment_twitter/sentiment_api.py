import requests


def get_sentiments(text_array):
    base_sentiment_url = "http://www.sentiment140.com/api/bulkClassifyJson"
    r = requests.post(base_sentiment_url, data=text_array)
    sum = 0;
    count = 0;
    for entry in r.json()['data']:
        sum = sum + entry['polarity']
        count += 1
    return sum/count

