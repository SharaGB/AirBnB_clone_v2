#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False
                     ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False
                     ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    name = Column(String(128), nullable=False
                  ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    description = Column(String(1024), nullable=True
                         ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    number_rooms = Column(Integer, nullable=False, default=0
                          ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    number_bathrooms = Column(Integer, nullable=False, default=0
                              ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    max_guest = Column(Integer, nullable=False, default=0
                       ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    price_by_night = Column(Integer, nullable=False, default=0
                            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    latitude = Column(Float, nullable=True
                      ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0

    longitude = Column(Float, nullable=True
                       ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0

    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref="place"
                           ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place_amenities', viewonly=False)
    else:

        @property
        def amenities(self):
            """ Returns the list of Amenity instances """
            amenity_instances = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_instances.append(amenity)
            return amenity_instances

        @amenities.setter
        def amenities(self, value):
            """ Handles append method for adding an Amenity.id to the
                        attribute amenity_ids """
            if isinstance(value, Amenity):
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value)

        @property
        def reviews(self):
            """ Returns the list of Review instances """
            place_instances = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    place_instances.append(review)
            return place_instances
