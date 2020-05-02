#!/usr/bin/env python
import json
import yweather
import sys

import logging

from twitter.data import cache
from twitter.data.auth import tweeter_api
from twitter.util.constants import LOCATION_INDIA, TRENDS_VOLUME
from twitter.util.utility_functions import _parse_trends, get_location_from_woeid

sys.path.append(".")

api = tweeter_api()


def available_trend():
    """
    Returns the locations that Twitter has trending topic information for.
    The response is an array of “locations” that encode the location’s WOEID (a Yahoo! Where On Earth ID) and
    some other human-readable information such as a canonical name and country the location belongs in
    :return:
    """
    locations = api.trends_available()
    print(locations)


def trends_by_location(woeids=[LOCATION_INDIA]):
    """
    returns trending topics/hashtags
    :param woeid:
    :return:
    """
    trends = dict()

    for woeid in woeids:
        trends[woeid] = _trend_for_one_location(woeid)

    return trends


def _trend_for_one_location(woeid):
    # woeid_lookup("")
    if cache.get_cache(woeid) is None:
        logging.info("MISS: making trends_place api call for {}".format(get_location_from_woeid(woeid)))
        india_trends = api.trends_place(woeid)
        trends = json.loads(json.dumps(india_trends))
        fields = _parse_trends(trends[0])
        cache.update_cache(woeid, fields)
        return fields

    logging.info("HIT: trends_place api cache hit for {}".format(get_location_from_woeid(woeid)))
    fields = cache.get_cache(woeid)
    return fields


def woeid_lookup(country="IN"):
    client = yweather.Client()
    return client.fetch_woeid(country)


def print_user_details(user_name='gaganmani90'):
    user = api.get_user(user_name)
    print(user.screen_name)
    print(user.followers_count)
    print(user.friends_count)


def keySort(trend):
    return trend.volume


