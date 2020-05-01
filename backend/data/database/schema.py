import sqlite3
import os


def schema():
    with sqlite3.connect(os.path.join(os.path.dirname(__file__), 'pegasus.db')) as conn:
        cur = conn.cursor()

        sql_1 = """
        CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(120),
        );
        """

        sql_2 = """
        CREATE TABLE IF NOT EXISTS trips(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userid VARCHAR(120),
        start_time VARCHAR(120),
        end_time VARCHAR(120),
        start_station,
        end_station,
        FOREIGN KEY (userid) REFERENCES users(pk),
        FOREIGN KEY (start_station) REFERENCES tube_stations(pk),
        FOREIGN KEY (end_station) REFERENCES tube_stations(pk)
        );
        """

        sql_3 = """
        CREATE TABLE IF NOT EXISTS preferences(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userid VARCHAR(120),
        vegetarian INTEGER,
        italian INTEGER,
        kosher INTEGER,
        FOREIGN KEY (userid) REFERENCES users(pk)
        );
        """

        sql_4 = """
        CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userid VARCHAR(120),
        UNIQUE(name)
        );
        """
        sql_5 = """
        CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userid VARCHAR(120),
        UNIQUE(name)
        );
        """
        sql_6 = """
        CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userid VARCHAR(120),
        UNIQUE(name)
        );
        """
        sql_7 = """
        CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(120),
        UNIQUE(name)
        );
        """

        sql_8 = """
        CREATE TABLE IF NOT EXISTS preference_ids(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        attraction_name VARCHAR(120),
        attraction_id VARCHER(120),
        UNIQUE(attraction_id)
        );
        """

        sql_9 = """
        CREATE TABLE IF NOT EXISTS tube_stations(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        station_id INTEGER,
        complex_id INTEGER,
        gtfs_stop_id VARCHAR(3),
        division VARCHAR(3),
        line VARCHAR(40),
        stop_name VARCHAR(50),
        borough VARCHAR(2),
        daytime_routes VARCHAR(15),
        structure VARCHAR(10),
        gtfs_latitude REAL,
        gtfs_longitude REAL,
        north_direction_label VARCHAR(60),
        south_direction_label VARCHAR(60),
        UNIQUE(station_id)
        );
        """

        for sql in [sql_1, sql_2, sql_3, sql_4, sql_5, sql_6, sql_7, sql_8, sql_9]:
            cur.execute(sql)


if __name__ == '__main__':
    schema()
