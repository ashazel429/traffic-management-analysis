import sqlite3
from sqlite3 import Error

def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect('traffic_management_db.db')
    except Error as e:
        print(e)

    return conn

