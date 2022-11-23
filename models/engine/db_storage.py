#!/usr/bin/python3
"""This module defines a class to manage the database for hbnb clone"""
from sqlalchemy import create_engine, MetaData
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                               .format(user, pwd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            metadata_obj = MetaData()
            for t in metadata_obj:
                t.drop(engine, checkfirst=False)

    def all(self, cls=None):
        return
