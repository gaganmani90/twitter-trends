from twitter.util.constants import TREND_VOLUME, TREND_NAME, get_location_map
from twitter.model.trend import Trend


def _parse_trends(json_data):
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
    return trends


def trends_to_string_util(trendsMap):
    webpage = ''
    for location, trends in trendsMap.items():
        header = ''.join([get_location_from_woeid(location), ": "])
        body = '\n'.join(map(str, trends))
        webpage = header + body
    return webpage


def get_location_from_woeid(woied):
    return get_location_map()[woied]