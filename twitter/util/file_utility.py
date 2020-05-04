from pathlib import Path

from twitter.util.constants import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_location_json_path():
    folder = Path(ROOT_DIR + "/" + LOCATION_FILE_NAME).resolve()
    return folder


def get_log_config():
    path = Path(ROOT_DIR + "../../" + LOG_CONFIG_NAME).resolve()
    return path
