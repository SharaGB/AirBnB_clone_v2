#!/usr/bin/python3
""" New engine DBStorage for sqlalchemy"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy import MetaData
from logging import info

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = getenv('HBNB_MYSQL_USER')
pssw = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')

classes = {"City": City, "State": State, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """init"""
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """sum"""
        dictionary = {}
        for x in classes:
            if cls is None or cls is classes[x] or cls is x:
                data = self.__session.query(classes[x]).all()
                for element in data:
                    key = '{}.{}'.format(type(element).__name__, element.id)
                    dictionary[key] = element
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            info('DELETING...')
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # scop_session = scoped_session(session)
        # self.__session = scop_session()
        self.__session = session()

    def close(self):
        """ close session """
        self.__session.close()
