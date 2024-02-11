#!/usr/bin/python3
<<<<<<< HEAD
"""
class City that inherits from BaseModel
"""
=======
"""Defines the City class."""
>>>>>>> My first commit
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """
        Summary: define the City class that inherits from BaseModel
        Public class attributes:
            name string - empty string
            state_id - empty string (it will be the State.id)
    """
    name = ""
    state_id = ""
=======
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
>>>>>>> My first commit
