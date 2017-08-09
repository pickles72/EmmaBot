import tweepy
from secrets import *
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# Instantiates a client
client = language.LanguageServiceClient()

tweets = api.home_timeline()




for tweet in tweets:
    print(tweet.text)


    for key in key_words:
        if key in tweet.text.lower():
            ## Tweet at the person
            response = "@" + tweet.user.screen_name + " " + key_words[key]

            api.update_status(status=response, in_reply_to_status_id=tweet.id)
            continue
