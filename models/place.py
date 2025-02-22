#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship(
            "Review", backref='place', cascade='all, delete')
        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """Returns a list of Reviews instances
            with same place id as current"""
            from models import storage
            from models.review import Review

            list_reviews = []
            Reviews_ = storage.all(Review).values()
            for rev in Reviews_:
                if self.id == rev.place_id:
                    list_reviews.append(rev)
            return list_reviews

        @property
        def amenities(self):
            """returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id
            linked to the Place"""
            from models import storage
            from models.amenity import Amenity

            am_list = []
            Amenities_ = storage.all(Amenity).values()
            for am in Amenities_:
                if am.id in self.amenity_ids:
                    am_list.append(am)
            return am_list

        @amenities.setter
        def amenities(self, obj):
            """Amenities setter"""
            from models.amenity import Amenity

            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
