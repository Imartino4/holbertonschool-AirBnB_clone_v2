#!/usr/bin/python3
"""This module defines a class to manage the database for hbnb clone"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review


USER = os.getenv('HBNB_MYSQL_USER')
PWD = os.getenv('HBNB_MYSQL_PWD')
HOST = os.getenv('HBNB_MYSQL_HOST')
DB_NAME = os.getenv('HBNB_MYSQL_DB')


class DBStorage:
    """Database Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(USER, PWD, HOST, DB_NAME),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method return a dictionary with all cls objects"""

        classes = {"User": User, "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place, "Review": Review}

        cls_dict = {}

        if type(cls) is not str:
            cls = cls.__name__  # A veces pasan objeto y a veces string
        if cls:
            cls_objects_ = self.__session.query(classes[cls])
            for data in cls_objects_:
                cls_dict["{}.{}".format(cls, data.id)] = data
        else:
            for c in classes.values():
                for data in self.__session.query(c):
                    cls_dict[
                        "{}.{}".format(
                            data.__class__.__name__, data.id)] = data
        return cls_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(new_session)()

    def close(self):
        """close"""
        self.__session.remove()
