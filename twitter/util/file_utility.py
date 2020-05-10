from pathlib import Path

from twitter.util.constants import *


def get_location_json_path():
    folder = Path(ROOT + "/twitter/util/" + LOCATION_FILE_NAME).resolve()
    return str(folder)


def get_log_config():
    path = Path(ROOT + "/twitter/" + LOG_CONFIG_NAME).resolve()
    print(path)
    return str(path)
