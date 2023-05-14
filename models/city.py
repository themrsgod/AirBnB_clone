#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A model that represents a city within the application.

    Attributes:
        state_id (str): The id of the state the city is located in.
        name (str): The name of the city.
    """

    state_id: str = ""
    name: str = ""