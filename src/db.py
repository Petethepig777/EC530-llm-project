import sqlite3


def connect_db(db_path):
    return sqlite3.connect(db_path)


def execute_query(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def fetch_all(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()