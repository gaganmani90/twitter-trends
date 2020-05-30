import mysql.connector

from twitter.data.database.db import db_conn
from twitter.data.execution_time import timed
from twitter.main import app
from twitter.trends_logger import trends_logger
from twitter.util.file_utility import get_database_config


@timed
def connect():
    """
    set connection and cursor
    :return:
    """
    trends_logger.info("Connecting to maria db")
    conn = mysql.connector.connect(
        host=DB_CONFIG['Host'],
        user=DB_CONFIG['Username'],
        password=DB_CONFIG['Password']
    )
    cur = conn.cursor()
    if conn is not None:
        cur.execute("Use " + DB_CONFIG['Database'])
    trends_logger.info("connection successful, using database {}".format(DB_CONFIG['Database']))
    return conn, cur


DB_CONFIG = get_database_config()
db_connection, cursor = connect()


@timed
# TODO: move out
def show_tables():
    trends_logger.info("Show tables ")
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)


# TODO move out of this file
def create_table_places():
    with app.open_resource('data/database/createTableLocation.sql') as f:
        result = cursor.execute(f)

    trends_logger.info("Places_List created successfully. {} ".format(result))


@timed
def close_connection():
    if db_connection.is_connected():
        cursor.close()
        db_connection.commit()
        db_connection.close()
        trends_logger.info("MySQL connection is closed")


if __name__ == '__main__':
   # create_table_places()
    #show_tables()
    #close_connection()
    db_conn().cursor()
