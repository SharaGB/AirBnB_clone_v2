#!/usr/bin/python3
""" """
import unittest
from models.engine.db_storage import DBStorage


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    def test_DBStorage(self):
        """ """
        module_DB = len(DBStorage.__doc__)
        self.assertGreater(module_DB, 0)

        module_DB_class = len(DBStorage.__init__.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.new.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.save.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.delete.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.reload.__doc__)
        self.assertGreater(module_DB_class, 0)

        module_DB_class = len(DBStorage.all.__doc__)
        self.assertGreater(module_DB_class, 0)
