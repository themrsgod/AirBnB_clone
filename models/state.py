#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A model that represents a state within the application.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""