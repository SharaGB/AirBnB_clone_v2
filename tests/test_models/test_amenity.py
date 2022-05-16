#!/usr/bin/python3
""" """
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """ """

    def test_pep8_conformance_tests(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_amenity(self):
        """ Test that we conform to PEP8. """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_class_docstring(self):
        """ Test for the Amenity class docstring """
        self.assertIsNotNone(Amenity.__doc__, "amenity.py needs a docstring")
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_is_subclass(self):
        """ Check that Amenity is a subclass of BaseModel """
        self.assertTrue(issubclass(Amenity(), BaseModel))

    def test_is_subclass(self):
        """ Test that Amenity is a subclass of BaseModel """
        self.assertIsInstance(Amenity(), BaseModel)
        self.assertTrue(hasattr(Amenity(), "name"))
        self.assertTrue(hasattr(Amenity(), "id"))
        self.assertTrue(hasattr(Amenity(), "created_at"))
        self.assertTrue(hasattr(Amenity(), "updated_at"))
