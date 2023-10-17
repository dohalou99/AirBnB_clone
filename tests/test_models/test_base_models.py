#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    my_model = BaseModel()

    def test_B1(self):
        """ Test attributes value of a BaseModel instance """

        sfMd = self.my_model
        sfMd.name = "Holberton"
        sfMd.my_number = 89
        sfMd.save()
        my_model_json = sfMd.to_dict()

        self.assertEqual(sfMd.name, my_model_json['name'])
        self.assertEqual(sfMd.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(sfMd.id, my_model_json['id'])

    def test_func_Save(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        sfMd = self.my_model
        sfMd.first_name = "First"
        sfMd.save()
        d = datetime.datetime
        self.assertTrue(type(sfMd.id), str)
        self.assertTrue(type(sfMd.created_at), d)
        self.assertTrue(type(sfMd.updated_at), d)

        first_dict = sfMd.to_dict()

        sfMd.first_name = "Second"
        sfMd.save()
        sec_dict = sfMd.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
