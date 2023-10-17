#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    my_model = BaseModel()

    def test_A(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def test_B(self):
        """ Test save and reload functions """
        sfMd = self.my_model
        sfMd.full_name = "BaseModel Instance"
        sfMd.save()
        bm_dict = sfMd.to_dict()
        all_objs = storage.all()

        k = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(k in all_objs, True)

    def test_C(self):
        """ Test save, reload and update functions """
        sfMd = self.my_model
        sfMd.my_name = "First name"
        sfMd.save()
        bm_dict = sfMd.to_dict()
        all_objs = storage.all()

        k = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(k in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        sfMd.my_name = "Second name"
        sfMd.save()
        bm_dict = sfMd.to_dict()
        all_objs = storage.all()

        self.assertEqual(k in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Second name")

    def test_D(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_E(self):
        """verify if JSON exists"""
        sfMd = self.my_model
        sfMd.save()
        pthTeted = os.path.exists(storage._FileStorage__file_path)
        self.assertEqual(pthTeted, True)
        strFil = storage._FileStorage__objects
        self.assertEqual(storage.all(), strFil)

    def test_F(self):
        """test if reload """
        sfMd = self.my_model
        sfMd.save()
        pthTeted = os.path.exists(storage._FileStorage__file_path)
        self.assertEqual(pthTeted, True)
        stObj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(stObj, FileStorage._FileStorage__objects)
        storage.reload()
        for k, value in storage.all().items():
            self.assertEqual(stObj[k].to_dict(), value.to_dict())

    def test_1(self):
        """ Check save self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self)

        self.assertEqual(str(e.exception), msg)

    def test_2(self):
        """ Test if 'new' method is working good """
        sfMd = self.my_model
        varOne = sfMd.to_dict()
        new_k = varOne['__class__'] + "." + varOne['id']
        storage.save()
        with open("file.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_k]
        for k in new:
            self.assertEqual(varOne[k], new[k])


if __name__ == '__main__':
    unittest.main()
