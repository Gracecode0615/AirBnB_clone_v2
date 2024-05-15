#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes and deserializes objects back and forth
    from dictionary objects to json files and reverse.

    Attributes:
        __file_path (str): JSON file(a path)
        __objects (dict): saves objects in class.name and class.id format
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def _import_all_model_classes(cls):
        """
        import model classes.
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

    def all(self):
        """Return:the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        new object to be added to the __objects dictionary.

        Args:
            obj: adds this object.
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Converts __objects JSON file (__file_path)."""
        file_dict = FileStorage.__objects
        obj_dict = {obj: file_dict[obj].to_dict() for obj in file_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Converts the JSON file to __objects."""
        self._import_all_model_classes()
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj_id, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    if class_name not in globals():
                        self._import_all_model_classes()
                    model_class = globals()[class_name]
                    self.new(model_class(**obj_data))
        except FileNotFoundError:
            return
