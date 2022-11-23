#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.engine.file_storage import FileStorage
from sqlalchemy import create_engine


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    user = os.getenv('HBNB_MYSQL_USER')
    pwd = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getenv('HBNB_MYSQL_DB')
    engine = create_engine('mysql://{}:{}@{}/{}'.format(user, pwd, host, db))
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref='State')
    else:
        @property
        def cities(self):
            l_cities = []
            for city in FileStorage.all("City"):
                if self.id == city.state_id:
                    l_cities.append = city
            return l_cities
