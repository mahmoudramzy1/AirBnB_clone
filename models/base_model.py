#!/usr/bin/python3
"""base module"""

import uuid
import datetime
import models


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self,
                                k,
                                datetime.datetime.strptime(
                                    v,
                                    "%Y-%m-%dT%H:%M:%S.%f"
                                    ))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """repesentation of the object"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """save"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returs dict"""
        x = self.__dict__.copy()
        x["__class__"] = self.__class__.__name__
        x["created_at"] = x["created_at"].isoformat()
        x["updated_at"] = x["updated_at"].isoformat()
        return x
