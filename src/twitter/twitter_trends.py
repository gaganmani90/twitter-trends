#!/usr/bin/env python
import json
import yweather
import sys

import logging

from twitter import cache
from twitter.auth import tweeter_api
from twitter.constants import LOCATION_INDIA, TREND_NAME, TREND_VOLUME, TRENDS_VOLUME, TREND_COUNT

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


def trends_by_location(woeid=LOCATION_INDIA):
    """
    returns trending topics/hashtags
    :param woeid:
    :return:
    """
    # woeid_lookup("")
    if cache.get_cache(TRENDS_VOLUME) is None:
        logging.info("cache hit")
        india_trends = api.trends_place(woeid)
        trends = json.loads(json.dumps(india_trends))
        fields, size = parse_trends(trends[0])
        cache.update_cache(TRENDS_VOLUME, fields)
        cache.update_cache(TREND_COUNT, size)
        return fields, size

    fields = cache.get_cache(TRENDS_VOLUME)
    size = cache.get_cache(TREND_COUNT)
    return fields, size


def woeid_lookup(country="IN"):
    client = yweather.Client()
    return client.fetch_woeid(country)


def print_user_details(user_name='gaganmani90'):
    user = api.get_user(user_name)
    print(user.screen_name)
    print(user.followers_count)
    print(user.friends_count)


def parse_trends(json_data, field='name'):
    """
    parse the trends which have some volume
    :param json_data:
    :param field:
    :return:
    """
    trends_list = (json_data['trends'])
    # print(trends_list)
    trends = []
    for currTrend in trends_list:
        volume = currTrend[TREND_VOLUME]
        if volume is not None:
            trend = Trend(currTrend[TREND_NAME], volume)
            trends.append(trend)
    trends.sort()
    return trends, len(trends)


def keySort(trend):
    return trend.volume


class Trend:
    def __init__(self, name, volume="mock"):
        self.name = name if name is not None else ""
        self.volume = volume if volume is not None else 0

    def __str__(self):
        return "".join([self.name, ": ", str(self.volume)])

    def __eq__(self, other):
        return self.volume, self.name == other.volume, other.name

    def __lt__(self, other):
        return self.volume > other.volume
