import flag
from cachetools import cache, cached

from twitter.data.cache import flag_cache
from twitter.data.external_api.country_flags import country_flag


class LocationModel:
    _children = []

    def __init__(self, woeid, name):
        self.parent_woeid = woeid
        self.name = name

    def add_child(self, woeid, name):
        self._children.append(Location(woeid, name))

    @property
    def get_children(self):
        return self._children


class Location:
    def __init__(self, woeid, name='', country_code=''):
        self._woeid = woeid
        self._name = name
        self._country_code = country_code
        self.update_db()

    def update_db(self):
        pass

    @property
    def get_country_code(self):
        return self._country_code


    @property
    def name_with_flag(self):
        return country_flag(self.get_country_code) + "" + self.get_name

    @property
    def get_name(self):
        return self._name

    @property
    def get_woeid(self):
        return self._woeid

    def __eq__(self, other):
        return self._woeid == other._woeid

    def __hash__(self):
        return self._woeid

    def __str__(self):
        return self._name + ":" + str(self._woeid)
