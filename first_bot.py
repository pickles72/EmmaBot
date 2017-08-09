import tweepy
from secrets import *
from markovbot import markovbot35
import os

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = api.home_timeline()

# Initialise a MarkovBot instance
tweetbot = markovbot35.MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, u'158-0.txt')
book2 = os.path.join(dirname, u'1342-0.txt')
book3 = os.path.join(dirname, u'pg105.txt')
book4 = os.path.join(dirname, u'pg161.txt')

# Make your bot read the book!
tweetbot.read(book)
tweetbot.read(book2)
tweetbot.read(book3)
tweetbot.read(book4)


for tweet in tweets:
    print(tweet.text)

    if "tbhjuststop" in tweet.text:
        file = open('tweets.txt', 'r+')
        found = False
        for line in file:
            if tweet.text is line:
                found = True

        if not found:
            print(tweet.text)
            file.write(tweet.text + "\n")


    for key in key_words:
        if key in tweet.text.lower():
            ## Tweet at the person
            response = "@" + tweet.user.screen_name + " " + key_words[key]

            api.update_status(status=response, in_reply_to_status_id=tweet.id)
            continue
