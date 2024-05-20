#!/usr/bin/python3

"""
tests the Place class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
import json
import os


class TestPlace(unittest.TestCase):
    """
    tests the Place class
    """

    def setUp(self):
        """
        sets up the test
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

            self.instance_1 = Place()
            self.instace_2 = Place()

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
        self.assertEqual(type(self.instance_1.city_id), str)
        self.assertEqual(type(self.instance_1.user_id), str)
        self.assertEqual(type(self.instance_1.name), str)
        self.assertEqual(type(self.instance_1.description), str)
        self.assertEqual(type(self.instance_1.number_rooms), int)
        self.assertEqual(type(self.instance_1.number_bathrooms), int)
        self.assertEqual(type(self.instance_1.max_guest), int)
        self.assertEqual(type(self.instance_1.price_by_night), int)
        self.assertEqual(type(self.instance_1.latitude), float)
        self.assertEqual(type(self.instance_1.longitude), float)
        self.assertEqual(type(self.instance_1.amenity_ids), list)

    def test_has_attr(self):
        """
        tests the attributes are present
        """
        self.assertTrue(hasattr(self.instance_1, "city_id"))
        self.assertTrue(hasattr(self.instance_1, "user_id"))
        self.assertTrue(hasattr(self.instance_1, "name"))
        self.assertTrue(hasattr(self.instance_1, "description"))
        self.assertTrue(hasattr(self.instance_1, "number_rooms"))
        self.assertTrue(hasattr(self.instance_1, "number_bathrooms"))
        self.assertTrue(hasattr(self.instance_1, "max_guest"))
        self.assertTrue(hasattr(self.instance_1, "price_by_night"))
        self.assertTrue(hasattr(self.instance_1, "latitude"))
        self.assertTrue(hasattr(self.instance_1, "longitude"))
        self.assertTrue(hasattr(self.instance_1, "amenity_ids"))

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
