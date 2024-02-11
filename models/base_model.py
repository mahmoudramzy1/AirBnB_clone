#!/usr/bin/python3
"""base module"""

import uuid
import datetime


class BaseModel:
    """base class"""
    
    def __init__(self):
        """constructor"""
        self.id = uuid.uuid4()
        self.id = str(self.id)
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """repesentation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """save"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returs dict"""
        x = self.__dict__
        x["__class__"] = self.__class__.__name__
        x["created_at"] = x["created_at"].isoformat()
        x["updated_at"] = x["updated_at"].isoformat()
        return x
