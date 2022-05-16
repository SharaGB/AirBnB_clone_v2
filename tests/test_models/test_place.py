#!/usr/bin/python3
""" """
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
