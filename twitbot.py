import tweepy
import wordtest
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
consumer_key = os.getenv('Api_key')
consumer_secret = os.getenv('API_key_secret')
access_token = os.getenv('Access_token')
access_token_secret = os.getenv('Secret_access_token')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
item = api.get_user('lhUsiWrfIhaP8yR')


# checking my tweet
def tweet_upload():
	
	tweets = api.user_timeline(
		screen_name=item.screen_name,
		count=200,
		include_rts = False,
		tweet_mode = 'extended'
		)

	for info in tweets[:1]:
		# print('ID : {}'.format(info.id))
		# print(info.created_at)
		# print(info.full_text)
		api.update_status(
			wordtest.wordFinding((info.full_text[len(info.full_text)-1]))[0]
			)


