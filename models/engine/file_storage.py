#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Represents file storage class

    This class handles the storage and retrieval of objects to and from a JSON file.
    """

    # Class variable to store the path to the JSON file
    __file_path = "file.json"

    # Class variable to store the dictionary of objects
    __objects = {}

    def all(self):
        """ Returns a dictionary of objects

        Returns:
            A dictionary of all objects currently stored in the file. The dictionary keys are strings that combine 
            the name of the class and the object's `id` attribute.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object to the `__objects` dictionary

        Args:
            obj: The object to be added to the dictionary
        """
        # Generate a key for the object by combining the name of the class and the object's `id` attribute
        classname = obj.__class__.__name__
        key = "{}.{}".format(classname, obj.id)

        # Add the object to the dictionary using the generated key
        FileStorage.__objects[key] = obj

    def save(self):
        """ Saves all objects in the `__objects` dictionary to a JSON file """

        # Convert all objects to dictionaries using their `to_dict()` method
        object_dictionary = FileStorage.__objects
        json_object = {obj: object_dictionary[obj].to_dict(
        ) for obj in object_dictionary.keys()}

        # Write the dictionary of objects to the JSON file
        with open(FileStorage.__file_path, "w") as file_opened:
            json.dump(json_object, file_opened)

    def reload(self):
        """ Loads all objects from the JSON file back into memory as objects of their respective classes """

        try:
            # Load the dictionary of objects from the JSON file
            with open(FileStorage.__file_path, "r") as file_opened:
                object_dictionary = json.load(file_opened)

                # Create new objects of the correct class for each dictionary of object attributes in the loaded file
                for o in object_dictionary.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))

        except FileNotFoundError:
            # Handle the case where the JSON file doesn't exist yet
            print('Exception occured')
            return
