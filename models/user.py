#!/usr/bin/python3
<<<<<<< HEAD
"""
class User that inherits from BaseModel
"""
=======
"""Defines the User class."""
>>>>>>> My first commit
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """
        Summary: Definning the User class that inherits from BaseModel
        Public class attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
    """
=======
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

>>>>>>> My first commit
    email = ""
    password = ""
    first_name = ""
    last_name = ""
