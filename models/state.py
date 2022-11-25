#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
    else:
        name = ""
        
        @property
        def cities(self):
            """Getter method to return cities
            instances with current state_id"""
            l_cities = []
            for city in storage.all("City"): #Iria a FileStorage
                if self.id == city.state_id:
                    l_cities.append(city)
            return l_cities
