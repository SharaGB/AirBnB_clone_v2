#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ Class to define a state and its attributes"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Getter attribute cities that returns the list of City """
        city_instances = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
