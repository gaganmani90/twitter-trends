trends_cache = dict()


def update_cache(key, value):
    trends_cache[key] = value


def get_cache(key):
    if key in trends_cache.keys():
        return trends_cache[key]
    return None


def size():
    return len(trends_cache)


def invalidate():
    trends_cache.clear()
