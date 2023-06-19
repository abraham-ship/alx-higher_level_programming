#!/usr/bin/python3

"""tests for square"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """unittest for square class"""
    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_square_creation(self):
        """Test creation of Square instance"""
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_str(self):
        """test _str method"""
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")

    def test_square_update(self):
        """test update method"""
        s = Square(5, 2, 3, 4)
        s.update(6)
        self.assertEqual(s.id, 6)
        self.assertEqual(str(s), "[Square] (6) 2/3 - 5")

        s.update(6, 7)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 7)
        self.assertEqual(str(s), "[Square] (6) 2/3 - 7")

        s.update(6, 7, 8)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(str(s), "[Square] (6) 8/3 - 7")

        s.update(6, 7, 8, 9)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)
        self.assertEqual(str(s), "[Square] (6) 8/9 - 7")

    def test_square_to_dictionary(self):
        """test to_dictionary method"""
        s = Square(5, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
