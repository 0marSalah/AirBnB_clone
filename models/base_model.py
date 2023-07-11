#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self):
      """Initialize a new BaseModel."""
      self.id = str(uuid.uuid4())
      self.created_at = datetime.today()
      self.updated_at = datetime.today()
    
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
      
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict