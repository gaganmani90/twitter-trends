import datetime
from functools import wraps

from twitter.trends_logger import trends_logger


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = datetime.datetime.now()
        result = f(*args, **kwds)
        elapsed = datetime.datetime.now() - start
        trends_logger.info("{}{} took {} msec to finish".format(f.__name__, args,elapsed.microseconds / 1000))
        return result

    return wrapper
