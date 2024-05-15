#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    City is a subclass of base model

    Public instance attributes:
    state_id: empty string
    name: string - empty string
    """
    state_id = ""
    name = ""
