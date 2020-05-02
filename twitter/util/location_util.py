import json, os

from twitter.util.constants import *

_location_to_woeid = dict()
_woeid_to_location = dict()


def populate_location_map():
    file_location = os.path.join('..', LOCATION_PATH)
    with open(file_location) as json_file:
        locations_data = json.load(json_file)
        for location in locations_data:
            name = location[KEY_NAME]
            woeid = location[KEY_WOEID]
            _location_to_woeid[name] = woeid
            _woeid_to_location[woeid] = name
    return _location_to_woeid, _woeid_to_location


def get_location_to_woeid():
    if _location_to_woeid is not None:
        return _location_to_woeid
    else:
        populate_location_map()
        return _location_to_woeid


def get_woeid_to_location():
    if _woeid_to_location is not None:
        return _woeid_to_location
    else:
        populate_location_map()
        return _woeid_to_location

def get_location_from_woeid(woied):
    return _woeid_to_location[int(woied)]