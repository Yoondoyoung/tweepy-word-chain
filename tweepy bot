import tweepy

consumer_key = '9ud2EhpmOBMsxGucEJLXk28qU'
consumer_secret = 'mS4jGUEjHNMVTNc8gJlmNs1XXlBHrYazqQnl0Gcmg1qV4NOSi6'
access_token = '1377815830109380609-b8zknQfzDx7iMU1zfhALd2T7FSE2r9'
access_token_secret = '3e56s9rFvinIK9LRXClK2VBjOIP9h9VqmktWx9SvolByS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)