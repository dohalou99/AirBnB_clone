#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """user class test"""

    a = User()

    def test_A_1(self):
        """check if user exist"""
        b = self.a
        cls_nm = "<class 'models.user.User'>"
        self.assertEqual(str(type(b)), cls_nm)

    def test_B_1(self):
        """check if user inhert from basemode class"""
        b = self.a
        self.assertIsInstance(b, User)

    def test_C_1(self):
        """check if att exist"""
        b = self.a
        self.assertTrue(hasattr(b, 'email'))
        self.assertTrue(hasattr(b, 'first_name'))
        self.assertTrue(hasattr(b, 'password'))
        self.assertTrue(hasattr(b, 'last_name'))
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_D_1(self):
        """check if the att type is correct"""
        b = self.a
        d = datetime.datetime
        self.assertTrue(type(b.email), str)
        self.assertTrue(type(b.password), str)
        self.assertTrue(type(b.first_name), str)
        self.assertTrue(type(b.last_name), str)
        self.assertTrue(type(b.id), str)
        self.assertTrue(type(b.created_at), d)
        self.assertTrue(type(b.updated_at), d)


if __name__ == '__main__':
    unittest.main()
