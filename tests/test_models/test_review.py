#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """review class test"""

    a = Review()

    def test_A_1(self):
        """check if review exist"""
        b = self.a
        cls_nm = "<class 'models.review.Review'>"
        self.assertEqual(str(type(b)), cls_nm)

    def test_B_1(self):
        """check if review inhert from basemode class"""
        b = self.a
        self.assertIsInstance(b, Review)

    def test_C_1(self):
        """check if att exist"""
        b = self.a
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'place_id'))
        self.assertTrue(hasattr(b, 'user_id'))
        self.assertTrue(hasattr(b, 'text'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_D_1(self):
        """check if the att type is correct"""
        b = self.a
        d = datetime.datetime
        self.assertTrue(type(b.id), str)
        self.assertTrue(type(b.place_id), str)
        self.assertTrue(type(b.user_id), str)
        self.assertTrue(type(b.text), str)
        self.assertTrue(type(b.created_at), d)
        self.assertTrue(type(b.updated_at), d)


if __name__ == '__main__':
    unittest.main()
