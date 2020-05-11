from .parent import ORM
from math import cos, radians


class TubeStations(ORM):
    """
    Only find_one is to be used.
    """
    tablename = 'tube_stations'
    fields = [
        'station_id', 'complex_id', 'gtfs_stop_id',
        'division', 'line', 'stop_name', 'borough',
        'daytime_routes', 'structure', 'gtfs_latitude',
        'gtfs_longitude', 'north_direction_label',
        'south_direction_label'
    ]
    filepath = ''

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

    @classmethod
    def find_closest(cls, lat, lon):
        station_list = TubeStations.find_all(1, 1)
        for station in station_list:
            # Length in meters of 1° of latitude = always 111.32 km
            # Length in meters of 1° of longitude = 40075 km * cos( latitude ) / 360
            latitude = abs(abs(float(station.gtfs_latitude)) - abs(lat)) * 111.32
            longitude = abs(abs(float(station.gtfs_longitude)) - abs(lon)) * cos(radians(latitude)) * 40075 / 360
            station.dist = (longitude ** 2 + latitude ** 2) ** 0.5
        x = sorted(station_list, key=(lambda x: x.dist))
        return x[0] if x[0].dist < 0.2 else None
