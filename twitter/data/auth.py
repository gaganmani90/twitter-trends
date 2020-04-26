import tweepy
from twitter import config


def tweeter_api():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_key, config.access_secret)

    api = tweepy.API(auth)
    return api
