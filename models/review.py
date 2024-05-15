#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Public instance attributes:
    place_id: string - empty string for Place.id
    user_id: String - for User.id
    text: an empty string
    """

    place_id = ""
    user_id = ""
    text = ""
