import tweepy
import key

consumer_key = key.consumer_key
consumer_secret = key.consumer_secret
access_token = key.access_token
access_token_secret = key.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
item = api.get_user('lhUsiWrfIhaP8yR')


# twitting

api.update_status('nothing')


# checking my tweet

tweets = api.user_timeline(
	screen_name=item.screen_name,
	count=200,
	include_rts = False,
	tweet_mode = 'extended'
	)

for info in tweets[:3]:
	print('ID : {}'.format(info.id))
	print(info.created_at)
	print(info.full_text)
	print("\n")

