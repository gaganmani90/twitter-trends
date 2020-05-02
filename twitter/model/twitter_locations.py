from twitter.data.auth import tweeter_api

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