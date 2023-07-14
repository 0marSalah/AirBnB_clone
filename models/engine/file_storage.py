#!/usr/bin/python3
""" FileStorage Class """

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
    
    def save(self):
        """Serialize __objects to the JSON file __file_path.""" 
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj_dict = json.load(f)
            for value in new_obj_dict.values():
                class_Name = value["__class__"]
                self.new(eval(class_Name)(**value))
        except FileNotFoundError:
            pass