from twitter.data.database.db import DBConnection
from twitter.util.constants import TREND_VOLUME, TREND_NAME
from twitter.model.trend import Trend
from twitter.util.location_util import location_from_woeid
import time


def _parse_trends(woeid, json_data) -> list:
    """
    parse the trends which have some volume
    :param json_data:
    :param field:
    :return:
    """
    trends_list = (json_data['trends'])
    trends = []
    for currTrend in trends_list:
        volume = currTrend[TREND_VOLUME]
        if volume is not None:
            trend = Trend(currTrend[TREND_NAME], volume)
            trends.append(trend)
            query = "insert into trends (woeid, volume, time, topic) values (%s, %s,%s,%s)"
            val = (woeid, volume, time.strftime('%Y-%m-%d %H:%M:%S'), currTrend[TREND_NAME])
            DBConnection.execute_query(query, val)

    trends.sort()

    return trends


def trends_to_string_util(trendsMap):
    webpage = ''
    for location, trends in trendsMap.items():
        header = ''.join([location_from_woeid(location), ": "])
        body = '\n'.join(map(str, trends))
        webpage = header + body
    return webpage
