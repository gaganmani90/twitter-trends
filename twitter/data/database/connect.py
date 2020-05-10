import sqlite3

from twitter.trends_logger import trends_logger
from twitter.util.constants import *


class DBOperations:
    conn = None

    @staticmethod
    def getConnection():
        if DBOperations.conn is None:
            DBOperations.conn = sqlite3.connect(DB_NAME)
            trends_logger.info("Databse successfully connected to {}".format(DB_NAME))
        return DBOperations.conn

    @staticmethod
    def create_trend_table():
        connection = DBOperations.getConnection()
        query = '''create table {}
                (woeid int,
                location text,
                volume int)'''.format(TABLE_TREND)
        connection.execute(query)
        trends_logger.info("Table {} created successfully".format(TABLE_TREND))

    @staticmethod
    def close():
        if DBOperations.conn is not None:
            DBOperations.conn.close()