import tweepy
from secrets import *
import requests

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = api.home_timeline()

for tweet in tweets:

    if tweet.author.id == 1416289596:

        if not tweet.favorited:
            api.create_favorite(tweet.id)

            response = tweet.text

            response = "@Foshasta " + tweet.text

            if len(response) > 140:
                continue
            api.update_status(status=response)


    for key in key_words:
        if key in tweet.text.lower():
            ## Tweet at the person
            response = "@" + tweet.user.screen_name + " " + key_words[key]

            try:
                api.update_status(status=response, in_reply_to_status_id=tweet.id)
            except tweepy.TweepError:
                continue

            continue

