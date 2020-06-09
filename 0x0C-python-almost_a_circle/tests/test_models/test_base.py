#!/usr/bin/python3
""" Almost a circle project - test Cases

"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8

class TestBase(unittest.TestCase):
    """ Test cases for base.py

    """
    @classmethod
    def setUpClass(cls):
        """ Setting up before start all cases
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Executed after each test
        """
        Base.__Base__nb_objects = 0
        self.assertEqual(Base.__Base__nb_objects, 0)
    
    def test_init(self):
        """ Test instance creation with and with out id
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(44).id, 44)
        self.assertEqual(Base().id, 2)

    def test_init_excep(self):
        """ Tests raise exeption with more than 2 arguments
        """
        with self.assertRaises(TypeError) as e:
            Base(44, 44)
        msg = "__init__() takes from 1 to 2 positional arguments "
        msg += "but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_init_noint(self):
        """ [you can assume id is an integer and you don’t need
            to test the type of it] but let's test it
        """
        self.assertEqual(Base("test").id, "test")
    

if __name__ == '__main__':
    unittest.main()