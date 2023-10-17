#!/usr/bin/python3
"""
Unittest for place.py
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """place class test"""

    a = Place()

    def test_A_3(self):
        """check if place exist"""
        b = self.a
        cls_nm = "<class 'models.place.Place'>"
        self.assertEqual(str(type(b)), cls_nm)

    def test_B_3(self):
        """check if place inhert from basemode class"""
        b = self.a
        self.assertIsInstance(b, Place)

    def test_C_3(self):
        """check if att exist"""
        b = self.a
        self.assertTrue(hasattr(b, 'city_id'))
        self.assertTrue(hasattr(b, 'user_id'))
        self.assertTrue(hasattr(b, 'name'))
        self.assertTrue(hasattr(b, 'description'))
        self.assertTrue(hasattr(b, 'number_rooms'))
        self.assertTrue(hasattr(b, 'number_bathrooms'))
        self.assertTrue(hasattr(b, 'max_guest'))
        self.assertTrue(hasattr(b, 'price_by_night'))
        self.assertTrue(hasattr(b, 'latitude'))
        self.assertTrue(hasattr(b, 'longitude'))
        self.assertTrue(hasattr(b, 'amenity_ids'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))
        self.assertTrue(hasattr(b, 'id'))

    def test_D_3(self):
        """check if the att type is correct"""
        b = self.a
        d = datetime.datetime
        self.assertTrue(type(b.description), str)
        self.assertTrue(type(b.number_rooms), int)
        self.assertTrue(type(b.number_bathrooms), int)
        self.assertTrue(type(b.max_guest), int)
        self.assertTrue(type(b.city_id), str)
        self.assertTrue(type(b.user_id), str)
        self.assertTrue(type(b.name), str)
        self.assertTrue(type(b.price_by_night), int)
        self.assertTrue(type(b.latitude), float)
        self.assertTrue(type(b.longitude), float)
        self.assertTrue(type(b.amenity_ids), list)
        self.assertTrue(type(b.created_at), d)
        self.assertTrue(type(b.updated_at), d)


if __name__ == '__main__':
    unittest.main()
