#!/usr/bin/python3
""" Unittest StateClass """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    def setUp(self):
        """SetUp method used"""
        self.state1 = State()
        self.state1.name = "juan"

    def test_base_pep8(self):
        """Test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in file used"""
        self.assertIsNotNone(State.__doc__)

    def test_is_instance(self):
        """Test instantiation used"""
        self.assertIsInstance(self.state1, State)

    def test_attributes(self):
        """Test checks on attributes"""
        self.state1.save()
        state1_json = self.state1.to_dict()
        my_new_state = State(**state1_json)
        self.assertEqual(my_new_state.id, self.state1.id)
        self.assertEqual(my_new_state.created_at, self.state1.created_at)
        self.assertEqual(my_new_state.updated_at, self.state1.updated_at)
        self.assertIsNot(self.state1, my_new_state)

    def test_subclass(self):
        """Test checks on inheritance"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_save(self):
        """Test checks on save methodUsed"""
        variable_update = self.state1.updated_at
        self.state1.save()
        self.assertNotEqual(variable_update, self.state1.updated_at)
