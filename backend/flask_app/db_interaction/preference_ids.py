from .parent import ORM


class PreferenceIds(ORM):
    """
    Only find_one is to be used.
    """
    tablename = 'preference_ids'
    fields = [
        'attraction_name', 'attraction_id'
    ]
    filepath = ''

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.attraction_name = kwargs.get('attraction_name')
        self.attraction_id = kwargs.get('attraction_id')
