import tweepy
from textblob import TextBlob
import json
import re

# Twitter API credentials
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"
access_token = "your_access_token_here"
access_token_secret = "your_access_token_secret_here"

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create API object
api = tweepy.API(auth)

# search for tweets on a particular topic
query = "python"
tweets = api.search(q=query, lang="en", count=10)

# create a set to store unique tweets
unique_tweets = set()

# create a list to store the cleaned and analyzed data
data = []

# analyze each tweet and add to the data list
for tweet in tweets:
    # clean the tweet text by removing URLs, mentions, and symbols
    text = re.sub(r"http\S+", "", tweet.text)  # remove URLs
    text = re.sub(r"@\S+", "", text)  # remove mentions
    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)  # remove symbols
    text = re.sub(r"\s+", " ", text)  # remove extra spaces
    text = text.strip()  # remove leading/trailing spaces
    
    # skip duplicate tweets
    if text in unique_tweets:
        continue
    else:
        unique_tweets.add(text)
    
    # analyze the sentiment of the cleaned tweet text
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    
    # add the cleaned tweet text and sentiment to the data list
    if sentiment > 0:
        data.append({
            "text": text,
            "sentiment": "positive"
        })
    elif sentiment < 0:
        data.append({
            "text": text,
            "sentiment": "negative"
        })
    else:
        data.append({
            "text": text,
            "sentiment": "neutral"
        })

# write the cleaned and analyzed data to a JSON file
with open("twitter_sentiment.json", "w") as outfile:
    json.dump(data, outfile)
