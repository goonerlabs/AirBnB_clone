#!/usr/bin/python3

"""This class implements an amenity Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
