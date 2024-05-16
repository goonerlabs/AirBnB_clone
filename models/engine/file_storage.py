#!/usr/bin/python3

"""
File storage module
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file"""
        with open(self.__file_path, "w") as fd:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, fd)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as fd:
                for v in json.load(fd).values():
                    self.new(eval(v["__class__"])(**v))
        except FileNotFoundError:
            pass
