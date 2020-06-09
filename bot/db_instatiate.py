# db_instatiate.py
# Script to create a sqlite3 database instance for the app
import sqlite3
from sqlite3.dbapi2 import Error
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def create_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logger.info(
            f'Database created successfully. Sqlite version: {sqlite3.version}')
        return conn
    except Error as e:
        logger.error(e)


def create_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE 'quotes' (
            'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            'text'	TEXT NOT NULL UNIQUE)"""
        )
        logger.info('Table created successfully.')
    except Error as e:
        logger.error(e)


def main():
    conn = create_db('quotes.db')
    create_table(conn)


if __name__ == "__main__":
    main()
