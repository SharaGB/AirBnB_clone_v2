#!/usr/bin/python3
""" """
from os import getenv
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.place_id, None)
        else:
            self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.text, None)
        else:
            self.assertEqual(type(new.text), str)
