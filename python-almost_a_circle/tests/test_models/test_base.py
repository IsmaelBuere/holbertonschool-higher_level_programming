#!/usr/bin/python3
""" Module for test Base class """


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os


class TestBaseMethods(unittest.TestCase):
    """Test cases for the Base class methods."""

    def setUp(self):
        """Set up method to reset the number of objects before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for assigning a specific id."""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """Test for assigning the default id (incremental starting from 1)."""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """Test for id incrementation based on the number of objects."""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """Test for id mix, using specific and default ids."""
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """Test for assigning id as a string."""
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """Test for passing more than one argument."""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """Test for accessing private attributes."""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """Test saving to file for Square class."""
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """Test saving to file for Rectangle class."""
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()
