#!/usr/bin/python3

"""
tests the Review class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
import json
import os


class TestReview(unittest.TestCase):
    """
    tests the Review class
    """

    def setUp(self):
        """
        sets up the test
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")

            self.instance_1 = Review()
            self.instace_2 = Review()

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
        self.assertEqual(type(self.instance_1.place_id), str)
        self.assertEqual(type(self.instance_1.user_id), str)
        self.assertEqual(type(self.instance_1.text), str)


    def test_has_attr(self):
        """
        tests the attributes are present
        """
        self.assertTrue(hasattr(self.instance_1, "place_id"))
        self.assertTrue(hasattr(self.instance_1, "user_id"))
        self.assertTrue(hasattr(self.instance_1, "text"))


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
