#!/usr/bin/python3
"""
tests the Amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import json
import os


class TestAmenity(unittest.TestCase):
    """
    tests the Amenity class
    """

    def setUp(self):
        """
        sets up the test
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

            self.instance_1 = Amenity()
            self.instace_2 = Amenity()

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
        self.assertEqual(type(self.instance_1.name), str)

    def test_attr_present(self):
        """
        tests the attributes are present
        """
        self.assertTrue(hasattr(self.instance_1, "name"))

    def test_parent(self):
        """
        tests it inherits from BaseModel
        """
        self.assertTrue(issubclass(type(self.instance_1), BaseModel))
        self.assertIsInstance(self.instance_1, BaseModel)

    def test_attr_inheritance(self):
        """
        tests the attributes are inherited
        """
        self.assertTrue("id" in self.instace_2.__dict__)
        self.assertTrue("created_at" in self.instace_2.__dict__)
        self.assertTrue("updated_at" in self.instace_2.__dict__)


if __name__ == "__main__":
    unittest.main()
