#!/usr/bin/python3
"""
Unittests for BaseModel


"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Tests for BaseModel
    """
    def test_docstring(self):
        """
        Checks for docstring
        """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_pep8_basemodel(self):
        """
        tests pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(['models/base_model.py'])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    @classmethod
    def setUp(cls):
        """
        Setup Test
        """
        cls.new_base = BaseModel()
        cls.new_base.x = "x"
        cls.new_base.y = 100

   