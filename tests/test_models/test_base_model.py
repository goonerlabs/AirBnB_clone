#!/usr/bin/python3

"""
tests the BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    tests the BaseModel class
    """

    def setUp(self):
        """
        sets up the test
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

            self.instance_1 = BaseModel()
            self.instace_2 = BaseModel()

    def tearDown(self):
        """
        tears down the test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("file.json.bak"):
            os.rename("file.json.bak", "file.json")

        del self.instance_1
        del self.instace_2

    def test_attr_types(self):
        """
        tests the types of the attributes
        """
        self.assertEqual(type(self.instance_1.id), str)
        self.assertEqual(type(self.instance_1.created_at), datetime)
        self.assertEqual(type(self.instance_1.updated_at), datetime)
        self.assetEqual(type(self.instance_1), BaseModel)

    def test_dict_init(self):
        """
        tests the dictionary initialization
        """
        new_dict = self.instace_1.to_dict()
        temp_instace = BaseModel(**new_dict)

        self.assertEqual(self.instace_1.id, temp_instace.id)
        self.assertEqual(self.instace_1.created_at, temp_instace.created_at)
        self.assertEqual(self.instace_1.updated_at, temp_instace.updated_at)

    def test_str(self):
        """
        tests the __str__ method
        """
    tmp = f"[BaseModel] ({self.instace_1.id}) {self.instace_1.__dict__}"
    self.assertEqual(str(self.instace_1), tmp)

    def test_save(self):
        """
        tests the save method
        """
        self.instace_1.save()
        self.assertNotEqual(self.instace_1.created_at,
                            self.instace_1.updated_at)

        try:
            with open("file.json", "r") as f:
                my_file = json.load(f)
                v = my_file["BaseModel.{}".format(self.instace_1.id)]
                self.assertEqual(v, self.instace_1.to_dict())
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        """
        tests the to_dict method
        """
        new_dict = self.instace_1.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertIn("__class__", new_dict)
        self.assertIn("id", new_dict)
        self.assertIn("created_at", new_dict)
        self.assertIn("updated_at", new_dict)

    def test_id_is_unique(self):
        """
        tests the id is unique
        """
        self.assertNotEqual(self.instace_1.id, self.instace_2.id)


if __name__ == "__main__":
    unittest.main()
