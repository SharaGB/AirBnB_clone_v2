#!/usr/bin/python3
""" """
from os import getenv
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.city_id, None)
        else:
            self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.description, None)
        else:
            self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.number_rooms, None)
        else:
            self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.number_bathrooms, None)
        else:
            self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.max_guest, None)
        else:
            self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.price_by_night, None)
        else:
            self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.latitude, None)
        else:
            self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.longitude, None)
        else:
            self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "file":
            self.assertEqual(type(new.amenity_ids), list)
