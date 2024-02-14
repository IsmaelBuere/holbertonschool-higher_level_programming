#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestBase(unittest.TestCase):
    """Unit test class for the Base class."""

    def test_create_instance(self):
        """Test creating an instance with automatic id assignment."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        """Test creating an instance with a custom id."""
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_to_json_string(self):
        """Test converting a list of dictionaries to JSON string."""
        list_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(list_dicts)
        expected_json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_str, expected_json_str)

    def test_from_json_string(self):
        """Test converting a JSON string to list of dictionaries."""
        json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        list_dicts = Base.from_json_string(json_str)
        expected_list_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(list_dicts, expected_list_dicts)

if __name__ == '__main__':
    unittest.main()