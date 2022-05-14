#!/usr/bin/python3
""" """
import sys
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Amenity': Amenity,
    'Place': Place,
    'City': City,
    'Review': Review
}


class DBStorage:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """ """
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}', pool_pre_ping=True)
        # Drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
    # Faltaaaaaaaaaa :c

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)  # Make sure your Session is safe
        self.__session = Session()
