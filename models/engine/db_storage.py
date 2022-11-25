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
DB = os.getenv('HBNB_TYPE_STORAGE')


class DBStorage:
    """Database Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(USER, PWD, HOST, DB), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):  # Este tengo dudas si funciona, lo revisamos
        """This method return a dictionary with all cls objects"""

        # Para chequear que cls sea efectivamente una clase
        classes = {"User": User, "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place, "Review": Review}

        cls_dict = {}

        if cls != None and cls in classes.values():
            # hago un llamado de solo los objetos cls
            cls_objects_ = self.__session.query(classes[cls]).all()
            for data in cls_objects_:
                cls_dict[f"{cls}.{data.id}"] = data
        else:
            for c in classes.values():
                for data in self.__session.query(c).all:
                    cls_dict[f"{data.__class__.__name__}.{data.id}"] = data
        return cls_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):  # El init ejecuta esto
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)  # Crear todas las tablas
        # Crear la session
        self.__session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)  # no entendí bien que hace
        self.__session = Session
