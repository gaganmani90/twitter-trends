import json

from twitter.model.location_model import Location, LocationModel
from twitter.util.constants import *
from twitter.util.file_utility import get_location_json_path

_location_to_woeid = dict()
_woeid_to_location = dict()
_location_models = dict()


def populate_location_map():
    # file_location = os.path.join('..', LOCATION_PATH)
    file_location = get_location_json_path()
    with open(file_location) as json_file:
        locations_data = json.load(json_file)
        for location in locations_data:
            name = location[KEY_NAME]
            woeid = location[KEY_WOEID]
            parent_id = location[KEY_PARENT_ID]
            _location_to_woeid[name] = woeid
            _woeid_to_location[woeid] = name
            _update_location_model(name, woeid, parent_id)


def _update_location_model(name, woeid, parent_id):
    if parent_id == 0:
        location = Location(woeid, name)
        _location_models[location] = []
    elif parent_id == 1:
        location = Location(woeid, name)
        if location in _location_models:
            _location_models[location] = _location_models.pop(location)
        else:
            _location_models[location] = []
    else:
        _location_models.setdefault((Location(parent_id)), []).append(Location(woeid, name=name))


def location_models():
    return _location_models


def child_models(parent_id):
    return _location_models[Location(parent_id)]


def location_to_woeid_map():
    if _location_to_woeid is not None:
        return _location_to_woeid
    else:
        populate_location_map()
        return _location_to_woeid


def woeid_to_location_map():
    if _woeid_to_location is not None:
        return _woeid_to_location
    else:
        populate_location_map()
        return _woeid_to_location


def location_from_woeid(woied):
    return _woeid_to_location[int(woied)]
