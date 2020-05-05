from .parent import ORM


class Preferences(ORM):
    """
    Only save( => _insert, => _update) and find_all are to be used.
    """
    tablename = 'preferences'
    fields = [
        'userid', 'vegetarian', 'italian', 'kosher'
    ]
    filepath = ''

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.userid = kwargs.get('userid')
        self.vegetarian = kwargs.get('vegetarian')
        self.italian = kwargs.get('italian')
        self.kosher = kwargs.get('kosher')
