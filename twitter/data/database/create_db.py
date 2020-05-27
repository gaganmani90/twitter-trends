import mysql.connector

from data.execution_time import timed
from trends_logger import trends_logger
from util.file_utility import get_database_config


@timed
def connect():
    """
    set connection and cursor
    :return:
    """
    trends_logger.info("Connecting to maira db")
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
def create_table_places(cursor):
  mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS Places_List ( 
                                 woeid int(15) NOT NULL,
                                 name varchar(250) NOT NULL,
                                 country varchar(250) NOT NULL,
                                 parentid int(15) NOT NULL,
                                 PRIMARY KEY (woeid)) """

  result = cursor.execute(mySql_Create_Table_Query)
  trends_logger.info("Places_List created successfully. {} ".format(result))

@timed
def close_connection():
    if db_connection.is_connected():
        cursor.close()
        db_connection.commit()
        db_connection.close()
        trends_logger.info("MySQL connection is closed")


if __name__ == '__main__':
    show_tables()
    close_connection()
