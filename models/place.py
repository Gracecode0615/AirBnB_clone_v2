#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel.

    Public class attributes:
    city_id: empty string
    user_id: empty string: it will be the User.id
    name: string that will be displayed
    description: string that will be displayed
    number_rooms: integer that will be displayed
    number_bathrooms: integer that will be displayed
    max_guest: max guest
    price_by_night: integer that will be displayed
    latitude: float that will be displayed
    longitude: float that will be displayed
    amenity_ids: list of string that will be displayed
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
