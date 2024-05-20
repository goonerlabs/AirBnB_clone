#!/usr/bin/python3

"""
Test File Storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """
    def setUp(self):
        """
        Setup
        """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.bak")

        self.instance_1 = FileStorage()
        self.instance_2 = FileStorage()

    def tearDown(self):
        """
        Tear Down
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.bak"):
            os.rename("file.json.bak", "file.json")

        del self.instance_1
        del self.instance_2

    def test_attr(self):
        """
        Test Attr
        """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assetTrue(hasattr(self.instance_1, "all"))
        self.assetTrue(hasattr(self.instance_1, "new"))
        self.assetTrue(hasattr(self.instance_1, "save"))
        self.assetTrue(hasattr(self.instance_1, "reload"))

    def test_private_attrs(self):
        """
        Test Private attributes
        """
        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)
            print(FileStorage.__file_path)

    def test_all(self):
        """
        Test all
        """
        tmp = self.instance_1.all()
        self.assertIsNotNone(tmp)
        tmp_id = f"BaseModel.{self.instance_1.id}"
        self.assertIn(tmp_id, tmp)
        self.assertIsInstance(tmp, dict)

    def test_reload(self):
        """
        Test reload
        """
        self.instance_1.save()
        self.assertTrue(os.path.isfile("file.json"))
        tmp = BaseModel()
        tmp_id = f"BaseModel.{tmp.id}"
        tmp.save()
        del self.instance_1._FileStorage__objects[tmp_id]
        self.instance_1.reload()
        self.assertIn(tmp_id, self.instance_1.all())


if __name__ == "__main__":
    unittest.main()
