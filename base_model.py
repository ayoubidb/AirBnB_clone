#!/usr/bin/python3
<<<<<<< HEAD
"""
BaseModel class defining all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models
import json
isoform_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        Summary: The base class definition
        from which the other classes will inherit
        Attributes:
            id -> Public instance attributes
            created_at -> Public instance attributes
            updated_at -> Public instance attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the object/instance attributes
            id: contains the object's identification
            created_at: datetime which the object was created
            updated_at: datetime which the object was modified
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, isoform_time)
                elif key is "__class__":
                    pass
                elif key is not "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """ Writing the __str__ method """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Public instance methods:
            update  public instance attribute updated_at
            with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Public instance methods
            returns a dictionary that containins all keys/values
            of __dict__ of the instance with self.__dict__
            we are making a copy.
            This method will be the first piece of the
            serialization/deserialization process: create a dictionary
            representation with “simple object type” of our BaseModel
        """
        dic_BaseClass = self.__dict__.copy()
        dic_BaseClass["__class__"] = self.__class__.__name__
        dic_BaseClass["created_at"] = self.created_at.isoformat()
        dic_BaseClass["updated_at"] = self.updated_at.isoformat()
        return dic_BaseClass
=======
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> My first commit
