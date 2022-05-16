import pep8
import unittest
import console
from unittest import TestCase


class TestConsole(TestCase):
    """ Unittests """

    def test_pep8_conformance_tests(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_console(self):
        """ Test that we conform to PEP8. """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """ Test for the console.py module docstring """
        self.assertIsNotNone(console.__doc__,
                             "console.py file needs a docstrings")
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstrings")


if __name__ == '__main__':
    unittest.main()
