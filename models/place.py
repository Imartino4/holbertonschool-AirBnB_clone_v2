#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


# Many to many relationship - esta es la tabla que asocia las dos clases
if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey("ameinities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("Review", backref='place', cascade='delete')
    amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    @property
    def reviews(self):
        """Returns a list of Reviews instances 
        with same place id as current"""
        from models import storage

        list_reviews = []
        Reviews_ = storage.all("Review")
        for rev in Reviews_.values:
            if self.id == rev.place_id:
                list_reviews.append(rev)
        return list_reviews