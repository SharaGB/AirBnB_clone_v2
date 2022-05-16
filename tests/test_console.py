import os
import pep8
import json
import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime
from unittest import TestCase
from models.state import State
from console import HBNBCommand


class Test_pep8(TestCase):
    '''Test pep8'''
    def test_pep8(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")


class Test_docstring(TestCase):
    '''Test doc strings '''
    def test_docstring(self):
        """ Test doc strings """
        self.assertIsNotNone(State.__doc__)


class Test_console(TestCase):
    """ test class City """
    def setUp(self):
        """Clean code after each test
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage.FileStorage__objects = {}
        if os.path.isfile("salida"):
            os.remove("salida")

    def test_create(self):
        ''' test the method create'''
        # Chack if create the file.json
        os.system('echo create State name="California" \
                   | ./console.py > salida')
        self.assertTrue(os.path.isfile("file.json"))
        # check if key name exist.
        with open('file.json') as f:
            data = json.load(f)
            dict_value = data.values()
            for value in dict_value:
                self.assertTrue(('name' in value))


if __name__ == '__main__':
    unittest.main()
