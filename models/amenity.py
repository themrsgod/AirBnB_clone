#!/usr/bin/python3
"""Defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        id (str): The UUID of the amenity.
        created_at (datetime): The datetime when the amenity instance was created.
        updated_at (datetime): The datetime when the amenity instance was last updated.
        name (str): The name of the amenity.
    """

    name = ""