#!/usr/bin/env python
import json
import yweather
import sys

from twitter.auth import tweeter_api

sys.path.append(".")

api = tweeter_api()


def trends_by_location(woeid=2282863):
    # woeid_lookup("")
    india_trends = api.trends_place(woeid)
    trends = json.loads(json.dumps(india_trends))
    fields, size = parse_trends(trends[0])
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
    trends_list = (json_data['trends'])
    #print(trends_list)
    trends = []
    for currTrend in trends_list:
        trend = Trend(currTrend[field], currTrend['tweet_volume'])
        trends.append(trend)
    return trends, len(trends)


class Trend:
    def __init__(self, name, volume="mock"):
        self.name = name if name is not None else ""
        self.volume = volume if volume is not None else ""

    def __str__(self):
        return "".join([self.name, ": ", str(self.volume)])
