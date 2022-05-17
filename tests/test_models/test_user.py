#!/usr/bin/python3
""" """
from os import getenv
from models.user import User
from tests.test_models.test_base_model import test_basemodel


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.first_name, None)
        else:
            self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.last_name, None)
        else:
            self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.email, None)
        else:
            self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.password, None)
        else:
            self.assertEqual(type(new.password), str)
