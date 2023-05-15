#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents a storage engine for objects in a JSON file.

    The FileStorage class abstracts the implementation of storing and retrieving
    objects from a JSON file. It provides a dictionary-like interface to store
    and access objects by their IDs.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects in the storage.

        This method returns a dictionary of all objects currently stored in the
        storage, where each key is in the format <ClassName>.<object_id>.

        Returns:
            dict: A dictionary of all objects in the storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage.

        This method adds a new object to the storage, where the key is in the
        format <ClassName>.<object_id>.

        Args:
            obj (BaseModel): The object to add to the storage.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize objects in the storage to the JSON file.

        This method saves all objects in the storage to a JSON file specified by
        __file_path. The objects are serialized as dictionaries and saved to the
        file.

        Note:
            The JSON file is overwritten with the current contents of the storage.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize objects from the JSON file into the storage.

        This method deserializes objects from the JSON file specified by
        __file_path into the storage. The objects are deserialized from
        dictionaries and instantiated as objects.

        Note:
            If the JSON file does not exist, this method does nothing.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
