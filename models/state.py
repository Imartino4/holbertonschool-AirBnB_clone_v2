#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
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
