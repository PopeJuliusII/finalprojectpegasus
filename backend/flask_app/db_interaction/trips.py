from .parent import ORM


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
