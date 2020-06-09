# db_populate.py
# Script to populate the dabatase
import sqlite3
from sqlite3.dbapi2 import Error
import logging
from db import create_connection

logging.basicConfig(leval=logging.INFO)
logger = logging.getLogger()


def populate_db(db_file, quotes_file):
    with open(quotes_file, 'r') as f:
        quotes = f.readlines()
        conn = create_connection(db_file)
        cur = conn.cursor()
        for quote in quotes:
            try:
                cur.execute(f"INSERT INTO quotes(text) VALUES(?);", (quote,))
                conn.commit()
            except Error as e:
                logger.error(e)


def main():
    populate_db('bot/quotes.db', 'bot/quotes_file.txt')


if __name__ == '__main__':
    main()
