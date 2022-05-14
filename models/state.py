#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """ Getter attribute cities that returns the list of City """
            city_instances = []
            for city in models.storage.all(City).values():
                 if city.state_id == self.id:
                      city_instances.append(city)
            return city_instances
