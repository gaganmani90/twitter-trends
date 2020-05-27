from pathlib import Path
import configparser
from twitter.util.constants import *


def get_location_json_path():
    folder = Path(ROOT + "/twitter/util/" + LOCATION_FILE_NAME).resolve()
    return str(folder)


def get_log_config():
    path = Path(ROOT + "/twitter/" + LOG_CONFIG_NAME).resolve()
    print(path)
    return str(path)


def get_database_config():
    """
    This file needs to be created locally. It reads the database password file that contains
    server credentials.
    :return: config keys and values
    """
    config = configparser.ConfigParser()
    config.read(ROOT + "/twitter/" + 'password.ini')
    return config['database']
