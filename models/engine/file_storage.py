#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'Amenity': Amenity,
           'Place': Place, 'City': City, 'Review': Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns the list of objects of one type of class """
        if cls is not None:
            temp = {}
            for key, val in FileStorage.__objects.items():
                if isinstance(val, cls):
                    temp[key] = val
            return temp
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)"""
        correct_dict = {}
        for key in self.__objects:
            correct_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(correct_dict, file)

    def reload(self):
        """Deserializes the JSON file to
        __objects (only if the JSON file
        (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                diction = json.load(file)
            for key in diction:
                self.__objects[key] = classes[diction[key]
                                              ['__class__']](**diction[key])
        except Exception:
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects if it’s inside - if obj is equal to None,
                    the method should not do anything """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self._objects:
                del self.__objects[key]

    def close(self):
        """ Deserializing the JSON file to objects """
        self.reload()
