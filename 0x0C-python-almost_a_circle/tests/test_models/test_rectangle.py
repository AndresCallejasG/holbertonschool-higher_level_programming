#!/usr/bin/python3
""" Almost a circle project - test Cases

"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8


class TestBase(unittest.TestCase):
    """ Test cases for rectangle.py

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
        pep8_result = pep8_style.check_files(['models/rectangle.py'])
        self.assertEqual(pep8_result.total_errors, 0, "fix pep8")

    def test_doc(self):
        """ Check for documentation
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_init(self):
        """ Test instance creation with and with out id
        """
        self.assertEqual(Rectangle(10, 2).id, 1)
        my_rect = Rectangle(10, 2, 0, 0, 44)
        self.assertEqual(my_rect.id, 44)
        self.assertEqual(my_rect.width, 10)
        self.assertEqual(my_rect.height, 2)
        self.assertEqual(my_rect.x, 0)
        self.assertEqual(my_rect.y, 0)
        self.assertEqual(Rectangle(2, 10).id, 2)

    def test_init_excep(self):
        """ Tests raise exception with less than 2 arguments
        """
        with self.assertRaises(TypeError) as e:
            Rectangle(32)
        msg = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), msg)

    def test_width(self):
        """ width must be an integer > 0
        """
        with self.assertRaises(TypeError) as e:
            Rectangle("str", 10)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)
        with self.assertRaises(TypeError) as e:
            Rectangle({}, 10)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)
        with self.assertRaises(TypeError) as e:
            Rectangle([], 10)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)
        with self.assertRaises(TypeError) as e:
            Rectangle((), 10)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 10)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_height(self):
        """ height must be an integer > 0
        """
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "str")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(10, {})
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(10, ())
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(10, [])
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle(5, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_x(self):
        """ x must be an integer >= 0
        """
        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, "str")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, {})
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, ())
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, [])
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle(4, 4, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_y(self):
        """ y must be an integer >= 0
        """
        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, 0, "str")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, 0, {})
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, 0, ())
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(4, 4, 0, [])
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle(4, 4, 0, -2)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
