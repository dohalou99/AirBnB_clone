#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """city class test"""

    a = City()

    def test_A_2(self):
        """check if city exist"""
        b = self.a
        cls_nm = "<class 'models.city.City'>"
        self.assertEqual(str(type(b)), cls_nm)

    def test_B_2(self):
        """check if city inhert from basemode class"""
        b = self.a
        self.assertIsInstance(b, City)

    def test_C_2(self):
        """check if att exist"""
        b = self.a
        self.assertTrue(hasattr(b, 'state_id'))
        self.assertTrue(hasattr(b, 'name'))
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_D_2(self):
        """check if the att type is correct"""
        b = self.a
        d = datetime.datetime
        self.assertTrue(type(b.state_id), str)
        self.assertTrue(type(b.name), str)
        self.assertTrue(type(b.id), str)
        self.assertTrue(type(b.created_at), d)
        self.assertTrue(type(b.updated_at), d)


if __name__ == '__main__':
    unittest.main()
