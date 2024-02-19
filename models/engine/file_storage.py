#!/usr/bin/python3

"""module to serialize and deserialize objects"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """class to store objects in file"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set obj in __object with key <object class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj
    
    def save(self):
        """selrialize objects and save it to file_path"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as fs:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, fs)
    
    def reload(self):
        """desrialize the json file if exists"""
        try:    
            with open(FileStorage.__file_path) as fd:
                des_obj = json.load(fd)
                for o in des_obj.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
