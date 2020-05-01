import sqlite3
import csv
import os
from foursquare_categories import scrape_foursquare_categories


def seed():
    with sqlite3.connect(os.path.join(os.path.dirname(__file__), 'pegasus.db')) as conn:
        cur = conn.cursor()
        for entry in scrape_foursquare_categories():

            sql = """
            INSERT INTO preference_ids
            (attraction_name,
            attraction_id)
            VALUES(?, ?)
            ;
            """

            cur.execute(sql, entry)

        with open(os.path.join(os.path.dirname(__file__), 'Stations.csv'), 'r') as f:
            read_er = csv.DictReader(f)
            for row in read_er:

                sql = """
                INSERT INTO tube_stations
                (station_id, complex_id, gtfs_stop_id, division, line,
                stop_name, borough, daytime_routes, structure, gtfs_latitude,
                gtfs_longitude, north_direction_label, south_direction_label)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ;
                """

                cur.execute(sql, tuple(row.values()))


if __name__ == '__main__':
    seed()
