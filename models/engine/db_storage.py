#!/usr/bin/python3
"""This module defines a class to manage the database for hbnb clone"""
from sqlalchemy import create_engine, MetaData
import os
from sqlalchemy.orm import sessionmaker, scoped_session


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            """metadata_obj = MetaData()
            for t in metadata_obj:
                t.drop(self.__engine, checkfirst=False)""" #El checker dio error aca, pruebo con la siguiente linea
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None): #Este tengo dudas si funciona, lo revisamos
        """This method return a dictionary wit all cls objects"""
        cls_dict = {}
        
        if cls:
            cls_objects_ = self.__session.query(cls).all() #hago un llamado de solo los objetos cls
            for data in cls_objects_:
                cls_dict[f"{cls}.{data.id}"] = data
        else:
            for data in self.__session.query().all:
                cls_dict[f"{data.__class__.__name__}.{data.id}"] = data
        return cls_dict
    
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit(obj)
    
    def delete(self, obj=None):
        """Deletes obj from current database session"""
        if obj != None:
            self.__session.delete(obj)
            self.save()
    
    def reload(self): #El init ejecuta esto 
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)  # Crear todas las tablas
        # Crear la session
        self.__session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session) #no entendí bien que hace