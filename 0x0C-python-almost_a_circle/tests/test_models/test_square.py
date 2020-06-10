#!/usr/bin/python3
""" Almost a circle project - test Cases

"""


import unittest
from models.base import Base
from models.square import Square
import pep8


class TestBase(unittest.TestCase):
    """ Test cases for square.py

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
        pep8_result = pep8_style.check_files(['models/square.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_init(self):
        """ Test instance creation with and with out id
        """
        self.assertEqual(Square(5).id, 1)
        my_square = Square(2, 0, 0, 44)
        self.assertEqual(my_square.id, 44)
        self.assertEqual(my_square.size, 2)
        self.assertEqual(my_square.x, 0)
        self.assertEqual(my_square.y, 0)
        self.assertEqual(Square(3, 1, 3).id, 2)

    def test_init_excep(self):
        """ Tests raise exeption without size
        """
        with self.assertRaises(TypeError) as e:
            Square()
        msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
