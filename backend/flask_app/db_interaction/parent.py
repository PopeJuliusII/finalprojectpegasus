import os
import sqlite3


class ORM:

    def __init__(self, **kwargs):
        raise NotImplementedError

    def insert(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            fieldslist = ", ".join(self.fields)
            question_marks = ", ".join(['?' for _ in self.fields[1:]]) + ', ?'
            sql = f"""INSERT INTO {self.tablename} ({fieldslist}) VALUES({question_marks});"""
            values = list(self.__dict__.values())[1:]
            cursor.execute(sql, values)

    def update(self, field, value, field_two=1, value_two=1, order_by=''):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            fieldslist = "=?, ".join(self.fields[1:]) + '=?'
            sql = f"""
            UPDATE {self.tablename}
            SET {fieldslist}
            WHERE {field}={value} AND {field_two}={value_two}
            {order_by}
            ;"""
            values = list(self.__dict__.values())[2:]
            cursor.execute(sql, values)

    def delete(self, field, value, field_two=1, value_two=1):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            sql = f"""
            DELETE FROM {self.tablename}
            WHERE {field}=? AND {field_two}=?;"""
            cursor.execute(sql, (value, value_two))

    @classmethod
    def find_all(cls, field, value):
        sql = f"""SELECT * FROM {cls.tablename} WHERE {field}=?;"""
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sql, (value,))
            rows = cursor.fetchall()
            return [cls(**row) for row in rows] if rows else None

    @classmethod
    def find_one(cls, field, value):
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE {field}=?;"""
            cursor.execute(sql, (value,))
            row = cursor.fetchone()
            return cls(**row)
