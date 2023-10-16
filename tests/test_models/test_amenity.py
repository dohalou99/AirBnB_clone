#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """amenity class test"""

    a = Amenity()

    def test_A_1(self):
        """check if amenity exist"""
        b = self.a
        cls_nm = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(b)), cls_nm)

    def test_B_1(self):
        """check if amenity inhert from basemode class"""
        b = self.a
        self.assertIsInstance(b, Amenity)

    def test_C_1(self):
        """check if att exist"""
        b = self.a
        self.assertTrue(hasattr(b, 'name'))
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_D_1(self):
        """check if the att type is correct"""
        b = self.a
        d = datetime.datetime
        self.assertTrue(type(b.name), str)
        self.assertTrue(type(b.id), str)
        self.assertTrue(type(b.created_at), d)
        self.assertTrue(type(b.updated_at), d)


if __name__ == '__main__':
    unittest.main()
