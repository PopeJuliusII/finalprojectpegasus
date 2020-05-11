from .parent import ORM
import sqlite3


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

    @classmethod
    def get_id(cls, name):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT attraction_id
            FROM preference_ids
            WHERE attraction_name
            LIKE "%{ name }%"
            LIMIT 1
            ;"""
            cursor.execute(sql)
            id = cursor.fetchone()
            return id
