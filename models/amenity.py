#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.place import association_table


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    # place_amenities = relationship("Place", secondary=association_table)
