#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state')
        
    @property
    def cities(self):
        """Getter method to return cities
        instances with current state_id"""
        from models import storage
        l_cities = []
        for city in storage.all("City"):
            if self.id == city.state_id:
                l_cities.append(city)
        return l_cities
