#!/usr/bin/env python
import json
import sys

from cachetools import cached

from twitter.data.cache import trends_cache
from twitter.data.external_api.tweepy_caller import trends_place
from twitter.trends_logger import trends_logger
from twitter.util.constants import *
from twitter.util.location_util import location_from_woeid
from twitter.util.utility_functions import _parse_trends

sys.path.append(".")


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
    """
    returns list of Trends for given location
    :param woeid: geo location such as 1 fot Worldwide
    :return:
    """
    trends_logger.info("Twitter API call: trends_place api call for {}".format(location_from_woeid(woeid)))
    india_trends = trends_place(woeid)
    trends = json.loads(json.dumps(india_trends))
    fields = _parse_trends(trends[0])
    return fields
