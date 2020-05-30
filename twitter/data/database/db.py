from flaskext.mysql import MySQL

from twitter.trends_logger import trends_logger
from twitter.util.constants import ENABLE_DB


class DBConnection(object):
    connection = None
    mysql = None

    @classmethod
    def get_connection(cls, new=False):
        if cls.mysql is None:
            return None
        if new or not cls.connection:
            cls.connection = cls.mysql.connect()
        return cls.connection

    @classmethod
    def init_db(cls, app):
        if cls.mysql is None:
            trends_logger.info("Initializing database")
            cls.mysql = MySQL()
            app.config['MYSQL_DATABASE_USER'] = 't7c7qgc22zuc0lzp'
            app.config['MYSQL_DATABASE_PASSWORD'] = 'o06hrt33tcioas7a'
            app.config['MYSQL_DATABASE_DB'] = 'g6jx3b8h1osgnhvi'
            app.config['MYSQL_DATABASE_HOST'] = 'u3r5w4ayhxzdrw87.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
            cls.mysql.init_app(app)
            cls.connection = cls.mysql.connect()

    @classmethod
    def close(cls):
        trends_logger.info("Closing database connection ...")
        if cls.connection is not None:
            cls.connection.close()

    @classmethod
    def execute_query(cls, query, val):
        if ENABLE_DB:
            trends_logger.debug("Executing query: {}, value: {}".format(query, val))
            cursor = cls.connection.cursor()
            cursor.execute(query, val)
            cls.connection.commit()
