import os
import sqlite3
from .parent import ORM


class TubeStations(ORM):
    tablename = 'tube_stations'
    fieldnames = [
        'station_id', 'complex_id', 'gtfs_stop_id',
        'division', 'line', 'stop_name', 'borough',
                    'daytime_routes', 'structure', 'gtfs_latitude',
                    'gtfs_longitude', 'north_direction_label',
                    'south_direction_label'
    ]

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.station_id = kwargs.get('station_id')
        self.complex_id = kwargs.get('complex_id')
        self.gtfs_stop_id = kwargs.get('gtfs_stop_id')
        self.division = kwargs.get('division')
        self.line = kwargs.get('line')
        self.stop_name = kwargs.get('stop_name')
        self.borough = kwargs.get('borough')
        self.daytime_routes = kwargs.get('daytime_routes')
        self.structure = kwargs.get('structure')
        self.gtfs_latitude = kwargs.get('gtfs_latitude')
        self.gtfs_longitude = kwargs.get('gtfs_longitude')
        self.north_direction_label = kwargs.get('north_direction_label')
        self.south_direction_label = kwargs.get('south_direction_label')
