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
    def __init__(self, woeid, name=''):
        self._woeid = woeid
        self._name = name

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
        return self._name+":"+str(self._woeid)