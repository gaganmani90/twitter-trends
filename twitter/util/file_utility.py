import os
from pathlib import Path

from twitter.util.constants import LOCATION_FILE_NAME


def get_location_json_path():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    folder = Path(ROOT_DIR + "/" + LOCATION_FILE_NAME).resolve()
    return folder
