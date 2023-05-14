#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A model that represents a user account.

    Attributes:
        email (str): The email address associated with the user account.
        password (str): The password used to authenticate the user account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""