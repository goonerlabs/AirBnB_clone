#!/usr/bin/python3
"""
tests the User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import json
import os


class TestUser(unittest.TestCase):
    """
    tests the User class
    """

    def setUp(self):
        """
        sets up the test
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

            self.instance_1 = User()
            self.instace_2 = User()

    def tearDown(self):
        """
        tears down the test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
            os.rename("file.json.bak", "file.json")

            del self.instance_1
            del self.instace_2

    def test_attr_types(self):
        """
        tests the types of the attributes
        """
        self.assertEqual(type(self.instance_1.email), str)
        self.assertEqual(type(self.instance_1.password), str)
        self.assertEqual(type(self.instance_1.first_name), str)
        self.assertEqual(type(self.instance_1.last_name), str)

    def test_has_attr(self):
        """
        tests the attributes are present
        """
        self.assertTrue(hasattr(self.instance_1, "email"))
        self.assertTrue(hasattr(self.instance_1, "password"))
        self.assertTrue(hasattr(self.instance_1, "first_name"))
        self.assertTrue(hasattr(self.instance_1, "last_name"))

    def test_parent(self):
        """
        tests it inherits from BaseModel
        """

        self.assertTrue(issubclass(type(self.instance_1), BaseModel))
        self.assertIsInstance(self.instance_1, BaseModel)

    def test_inheritance(self):
        """
        tests it inherits from BaseModel
        """
        self.assertTrue("id" in self.instace_2.__dict__)
        self.assertTrue("created_at" in self.instace_2.__dict__)
        self.assertTrue("updated_at" in self.instace_2.__dict__)


if __name__ == "__main__":
    unittest.main()
