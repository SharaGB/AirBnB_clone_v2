#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
# from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Inherits from BaseModel and Base """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    # place_amenities = relationship('Place', secondary='place_amenity',
    #                                backref='amenities')
