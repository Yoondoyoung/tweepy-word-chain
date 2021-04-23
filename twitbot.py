import tweepy
import key
import test
consumer_key = key.consumer_key
consumer_secret = key.consumer_secret
access_token = key.access_token
access_token_secret = key.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
item = api.get_user('lhUsiWrfIhaP8yR')

# checking my tweet

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
		test.wordFinding((info.full_text[len(info.full_text)-1]))[0] 
		)


