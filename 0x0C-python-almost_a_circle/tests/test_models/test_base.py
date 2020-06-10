#!/usr/bin/python3
""" Almost a circle project - test Cases

"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import os.path
from os import path


class TestBase(unittest.TestCase):
    """ Test cases for base.py

    """
    @classmethod
    def setUp(cls):
        """ Setting up before start all cases
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Executed after each test
        """
        Base.__Base__nb_objects = 0
        self.assertEqual(Base.__Base__nb_objects, 0)

    def test_pep8(self):
        """ PEP 8 validation
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        pep8_result = pep8_style.check_files(['models/base.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

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
        self.assertEqual(Base(44.4).id, 44.4)
        self.assertEqual(Base({}).id, {})
        self.assertEqual(Base(()).id, ())
        self.assertEqual(Base([]).id, [])

    def test_to_json_string(self):
        """ method that returns JSON string representation
            of list_dictionaries
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(Base.to_json_string(json_dictionary)), str)

    def test_save_to_file(self):
        """ writes the JSON string representation of list_objs
            to a file
        """
        r1 = Rectangle(4, 4)
        Rectangle.save_to_file([r1])
        self.assertTrue(path.exists("Rectangle.json"))

    def test_from_json_string(self):
        """ returns the list of the JSON string representation
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """ returns an instance with all attributes already set
        """
        r1 = Rectangle(10, 7, 2, 8, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(str(r1) == str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """ returns a list of instances from a file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

if __name__ == '__main__':
    unittest.main()
