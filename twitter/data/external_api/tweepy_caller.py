from cachetools import cached

from twitter.data.auth import tweeter_api
from twitter.data.cache import trends_cache
from functools import wraps
from time import time

from twitter.data.execution_time import timed

api = tweeter_api()


@cached(trends_cache)
@timed
def trends_place(woeid=1):
    return api.trends_place(woeid)

@timed
def get_user(user_name='gaganmani90'):
    user = api.get_user(user_name)
    return user.screen_name, user.followers_count, user.friends_count
