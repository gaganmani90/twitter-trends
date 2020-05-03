import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
trends_logger = logging.getLogger("[Twitter Trends]")