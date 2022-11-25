#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models import storage

# Many to many relationship - esta es la tabla que asocia las dos clases
place_amenity = Table('place_amenity', Base.metadata,
                    Column(
                        'place_id', String(60), ForeignKey(
                        'places.id'), primary_key=True
                        ),
                    Column(
                        'amenity_id', String(60),
                        ForeignKey("ameinities.id"),
                        primary_key=True, nullable=False
                    ))

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
    reviews = relationship("Review", backref='place')
    amenities = relationship("Amenity", secondary=place_amenity,
                                  viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns a list of Reviews instances 
            with same place id as current"""
            list_reviews = []
            Reviews_ = storage.all("Review") #Aca tengo todos los reviews en diccionario
            for rev in Reviews_.values: #Recorro en la base de datos todas las instancias Review.
                if self.id == rev.place_id: #Comparo el id de la instancia actual con el de la base
                    list_reviews.append(rev)
            return list_reviews