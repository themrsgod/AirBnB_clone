#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A model that represents a rental property available for booking.

    Attributes:
        city_id (str): The ID of the city where the rental property is located.
        user_id (str): The ID of the user who owns the rental property.
        name (str): The name of the rental property.
        description (str): A detailed description of the rental property.
        number_rooms (int): The number of rooms available in the rental property.
        number_bathrooms (int): The number of bathrooms available in the rental property.
        max_guest (int): The maximum number of guests allowed to stay in the rental property.
        price_by_night (int): The price per night to rent the property.
        latitude (float): The latitude coordinate of the rental property.
        longitude (float): The longitude coordinate of the rental property.
        amenity_ids (list): A list of amenity IDs associated with the rental property.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
