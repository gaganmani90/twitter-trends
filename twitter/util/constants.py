LOCATION_INDIA = "23424848"  # PARENT ID
LOCATION_INDIA_NAGPUR = "2282863"
LOCATION_INDIA_JAIPUR = "2295401"
LOCATION_INDIA_LUCKNOW = "2295377"
LOCATION_INDIA_KANPUR = "2295378"
LOCATION_INDIA_PATNA = "2295381"
LOCATION_INDIA_RANCHI = "2295383"
LOCATION_INDIA_KOLKATA = "2295386"

TREND_NAME = 'name'
TREND_VOLUME = 'tweet_volume'

# CACHE KEYS
TRENDS_VOLUME = "trends"
TREND_COUNT = "size"


def get_location_map():
    location = dict()
    location["23424848"] = 'India'
    location["2282863"] = 'Nagpur'
    location["2295401"] = 'Jaipur'
    location["2295377"] = 'Lucknow'
    location["2295378"] = 'Kanpur'
    location["2295381"] = 'Patna'
    location["2295383"] = 'Ranchi'
    location["2295386"] = 'Kolkata'
    return location


