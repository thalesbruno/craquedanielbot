import sqlite3
from sqlite3.dbapi2 import Error
from random import randrange
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        logger.info(e)
    return conn

def select_quote():
    conn = create_connection("quotes.db")
    cur = conn.cursor()
    cur.execute("SELECT MIN(id), MAX(id) FROM quotes;")
    min_id, max_id = cur.fetchone()
    quote_id = randrange(min_id, max_id)
    cur.execute(f"SELECT text FROM quotes WHERE id={quote_id}")
    quote = cur.fetchone()[0]
    return quote
