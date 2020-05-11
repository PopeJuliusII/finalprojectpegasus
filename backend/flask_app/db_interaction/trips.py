from .parent import ORM
from arrow import utcnow


class Trips(ORM):
    """
    Only save( => _insert, => _update) and find_one are to be used.
    """
    tablename = 'trips'
    fields = [
        'userid', 'start_time', 'end_time',
        'start_station', 'end_station'
    ]
    filepath = ''

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.userid = kwargs.get('userid')
        self.start_time = kwargs.get('start_time')
        self.end_time = kwargs.get('end_time')
        self.start_station = kwargs.get('start_station')
        self.end_station = kwargs.get('end_station')

    @classmethod
    def new_entry(cls, station_name, uid):
        trip_list = cls.find_all('userid', uid)
        if trip_list is None:
            Trips(userid=uid, start_time=utcnow().timestamp, end_time=utcnow().timestamp, start_station=station_name, end_station=station_name).insert()
            return True
        else:
            trip_list.sort(key=(lambda x: -int(x.start_time)))
            print(trip_list[0].pk)
            if (utcnow().timestamp - int(trip_list[0].start_time)) <= 300 and station_name != trip_list[0].end_station:
                trip_list[0].end_time = utcnow().timestamp
                trip_list[0].end_station = station_name
                trip_list[0].update('userid', uid, 'start_time', trip_list[0].start_time)
                return True
            else:
                Trips(userid=uid, start_time=utcnow().timestamp, end_time=utcnow().timestamp, start_station=station_name, end_station=station_name).insert()
                return True
