#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A model that represents a review of a place.

    Attributes:
        place_id (str): The id of the place being reviewed.
        user_id (str): The id of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
