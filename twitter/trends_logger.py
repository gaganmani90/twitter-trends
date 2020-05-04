import logging
from logging.config import fileConfig

from twitter.util.file_utility import get_log_config

fileConfig(get_log_config(), disable_existing_loggers=False)
trends_logger = logging.getLogger("[Twitter Trends]")