import json
from models.base_model import BaseModel

class FileStorage:
    """
    Represents file storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary of objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects """
        classname = obj.__class__.__name__
        key = "{}.{}".format(classname,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        object_dictionary = FileStorage.__objects
        json_object = {obj: object_dictionary[obj].to_dict() for obj in object_dictionary.keys()}
        with open(FileStorage.__file_path, "w") as file_opened:
            json.dump(json_object, file_opened)

    def reload(self):
        """ Deserialize json file to objects"""
        try:
            with  open(FileStorage.__file_path, "r") as file_opened:
                object_dictionary = json.load(file_opened)
                for o in object_dictionary.values():
                    classname = o["__class__"]
                    #self.new(eval(classname)(**o))

        except FileNotFoundError:
            print('Exception occured')
            return

