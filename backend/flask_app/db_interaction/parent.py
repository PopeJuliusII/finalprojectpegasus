import os
import sqlite3


class ORM:
    """
    The parent class.
    """
    dbpath = ''
    tablename = ''
    fields = ['']
    pk = None

    def __init__(self, **kwargs):
        raise NotImplementedError

    def save(self):
        """
        Calls either the private function insert
        or the private function save depending on
        whether a pk is detected.
        """
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        """
        Adds the instance to the database as a new
        entry.
        """
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            fieldslist = ", ".join(self.fields)
            question_marks = ", ".join(['?' for _ in self.fields[1:]]) + ', ?'
            sql = f"""INSERT INTO {self.tablename} ({fieldslist}) VALUES({question_marks});"""
            values = list(self.__dict__.values())[1:]
            cursor.execute(sql, values)

    def _update(self):
        """
        Updates the corresponding pk's entry in the database.
        """
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            fieldslist = "=?, ".join(self.fields) + '=?'
            sql = f"""UPDATE {self.tablename} SET {fieldslist} WHERE pk=?;"""
            values = list(self.__dict__.values())[1:] + [self.pk]
            cursor.execute(sql, values)

    @classmethod
    def find_all(cls, field, value):
        """
        Shows all rows from the corresponding table.
        """
        sql = f"""SELECT * FROM {cls.tablename} WHERE {field}={value};"""
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [cls(**row) for row in rows]

    @classmethod
    def find_one(cls):
        """
        Shows all rows from the corresponding table.
        """
        sql = f"""SELECT * FROM {cls.tablename};"""
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [cls(**row) for row in rows]
