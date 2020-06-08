import sqlite3
from sqlite3.dbapi2 import Error
from random import randrange

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_quote(conn):
    cur = conn.cursor()
    cur.execute("SELECT MIN(id), MAX(id) FROM quotes;")
    min_id, max_id = cur.fetchone()
    quote_id = randrange(min_id, max_id)
    cur.execute(f"SELECT text FROM quotes WHERE id={quote_id}")
    quote = cur.fetchone()[0]
    return quote

def main():
    database = "quotes.db"
    conn = create_connection(database)
    quote = select_quote(conn)
    return quote

if __name__ == "__main__":
    main()