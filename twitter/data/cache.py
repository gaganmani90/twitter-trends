from cachetools import TTLCache

from twitter.trends_logger import trends_logger

trends_cache = TTLCache(maxsize=1000, ttl=3600)
flag_cache = TTLCache(maxsize=1000, ttl=36000000000)


def update_cache(key, value):
    trends_logger.info("MISS: updating cache for key: {}, size: {}".format(key, size()))
    trends_cache[key] = value


def get_cache(key):
    if key in trends_cache.keys():
        trends_logger.info("HIT: found in cache for key: {}, size: {}".format(key, size()))
        return trends_cache[key]
    return None


def size():
    return len(trends_cache)


def invalidate():
    trends_logger.info("DANGER: invalidated cache manually, size: {}".format(size()))
    trends_cache.clear()
