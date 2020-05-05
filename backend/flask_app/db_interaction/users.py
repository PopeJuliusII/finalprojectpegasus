from .parent import ORM


class Users(ORM):
    """
    Only save( => _insert) and find_one are to be used.
    """
    tablename = 'users'
    fields = [
        'id', 'email'
    ]
    filepath = ''

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.id = kwargs.get('id')
        self.email = kwargs.get('email')
