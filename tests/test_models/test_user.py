#!/usr/bin/python3
import unittest
import pep8
import os
from models.user import User
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to delete a Module"""
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/user.py"
        file2 = "tests/test_models/test_user.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.user_1 = User()
        self.user_1.name = 'Jeniffer'
        self.user_1.lastname = "Vanegas"
        self.user_1.email = 'airbnb@holbertonshool.com'
        self.user_1.password = "root"
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ define class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ close the class """
        print("tearDownClass")

    def test_user_doc(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_place_city(self):
        """ check if the city name is create """
        self.user_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_1, "__init__"))
        self.assertTrue(hasattr(self.user_1, "email"))
        self.assertTrue(hasattr(self.user_1, "password"))
        self.assertTrue(hasattr(self.user_1, "first_name"))
        self.assertTrue(hasattr(self.user_1, "last_name"))

    def test_user_name(self):
        """ check if the name is create """
        self.assertEqual(self.user_1.name, 'Jeniffer')

    def test_user_lastname(self):
        """ chaeck if the lastname is create """
        self.assertEqual(self.user_1.lastname, "Vanegas")


