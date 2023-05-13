#!/usr/bin/python3
"""
Defines the base model
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Args: 
            *args (any):
            **kwargs (dic): dictionary of key/value pairs of attributes
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f" 
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    ### date = '2023-05-23' obje(23033232)
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            ##
            print("else")
            storage.new(self)

    def __str__(self):
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname,self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.now()
        # save 
        storage.save()

    def to_dict(self):
        """
        return a dictionary
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

