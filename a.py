import tweepy
from decouple import config

auth = tweepy.OAuthHandler(config('consumer_key'), config('consumer_secret'))
auth.set_access_token(config('access_token'), config('access_token_secret'))

api = tweepy.API(auth)

user_name = "@quleuber"
status_id = 1241445549209014284

status = api.get_status(status_id, tweet_mode='extended')

replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                        since_id=status_id, tweet_mode='extended').items()

for a in replies:
    print(a.full_text)
    print(a.id)
