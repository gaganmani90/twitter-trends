#!/usr/bin/env python
import json
import sys

import yweather
from cachetools import cached

from twitter.data.auth import tweeter_api
from twitter.data.cache import trends_cache
from twitter.trends_logger import trends_logger
from twitter.util.constants import *
from twitter.util.location_util import location_from_woeid
from twitter.util.utility_functions import _parse_trends

sys.path.append(".")

api = tweeter_api()


def trends_by_location(woeids=[LOCATION_WW]):
    """
    returns trending topics/hashtags
    :param woeid:
    :return:
    """
    trends = dict()

    for woeid in woeids:
        trends[woeid] = _trend_for_one_location(woeid)

    return trends


@cached(trends_cache)
def _trend_for_one_location(woeid):
    trends_logger.info("Twitter API call: trends_place api call for {}".format(location_from_woeid(woeid)))
    india_trends = api.trends_place(woeid)
    trends = json.loads(json.dumps(india_trends))
    fields = _parse_trends(trends[0])
    return fields


def woeid_lookup(country="IN"):
    client = yweather.Client()
    return client.fetch_woeid(country)


def print_user_details(user_name='gaganmani90'):
    user = api.get_user(user_name)
    print(user.screen_name)
    print(user.followers_count)
    print(user.friends_count)



