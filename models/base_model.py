#!/usr/bin/python3
"""this class is the parent of other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Attributes: Date format used for date string conversion"""

    def __init__(self, *args, **kwargs):
        """Creates a new instance(object) of BaseModel
           Args:
                -*args (any): Unused.
                --**kwargs (dict): Key/value pairs of attributes.
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, DATE_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """saves updates to filestorage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """a method that returns a string rep of the class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """to_dict return a dictionary that contains objects"""
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
