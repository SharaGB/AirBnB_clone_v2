#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship('Amenity', secondary='place_amenity', backref='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """ Returns the list of Review instances """
        place_instances = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                place_instances.append(review)
        return place_instances

    @property
    def amenities(self):
        """ Returns the list of Amenity instances """
        self.amenity_ids = models.storage.all(Amenity)
        return self.amenity_ids
        # amenity_instances = []
        # for amenity in models.storage.all(Amenity).values():
        #     if amenity.amenity_id == self.id:
        #         amenity_instances.append(amenity)
        # return amenity_instances

    @amenities.setter
    def amenities(self, value):
        """ Handles append method for adding an Amenity.id to the attribute amenity_ids """
        if value.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(value)
