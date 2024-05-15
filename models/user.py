#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.

    Public instance attributes:
    email: An empty string
    password: An empty string
    first_name: An empty string
    last_name: An empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
