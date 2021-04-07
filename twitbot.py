import tweepy

consumer_key = '9ud2EhpmOBMsxGucEJLXk28qU'
consumer_secret = 'mS4jGUEjHNMVTNc8gJlmNs1XXlBHrYazqQnl0Gcmg1qV4NOSi6'
access_token = '1377815830109380609-b8zknQfzDx7iMU1zfhALd2T7FSE2r9'
access_token_secret = '3e56s9rFvinIK9LRXClK2VBjOIP9h9VqmktWx9SvolByS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
item = api.get_user('lhUsiWrfIhaP8yR')


# twitting

# api.update_status('test')


# checking my tweet

# tweets = api.user_timeline(
# 	screen_name=item.screen_name,
# 	count=200,
# 	include_rts = False,
# 	tweet_mode = 'extended'
# 	)

# for info in tweets[:3]:
# 	print('ID : {}'.format(info.id))
# 	print(info.created_at)
# 	print(info.full_text)
# 	print("\n")

