from .parent import ORM


class Saved(ORM):
    """
    Only save( => _insert, => _update) and delete and find_all are to be used.
    """
    tablename = 'saved'
    fields = [
        'userid', 'name', 'category', 'address',
        'latitude', 'longitude'
    ]
    filepath = ''

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.userid = kwargs.get('userid')
        self.name = kwargs.get('name')
        self.category = kwargs.get('category')
        self.address = kwargs.get('address')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
