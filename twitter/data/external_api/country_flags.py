import flag
from cachetools import cached

from twitter.data.cache import flag_cache


@cached(flag_cache)
def country_flag(code):
    if code is None:
        return ''
    try:
        value = flag.flag(code)
    except:  # invalid code
        value = ''
    return value
