#!/usr/bin/python3
""" """
from os import getenv
from models.city import City
from tests.test_models.test_base_model import test_basemodel


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.state_id, None)
        else:
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)
