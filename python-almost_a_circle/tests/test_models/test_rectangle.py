#!/usr/bin/python3
""" Module for test Rectangle class """


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test initialization of Rectangle."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, None)

    def test_area(self):
        """Test calculation of Rectangle's area."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test displaying the Rectangle."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test string representation of Rectangle."""
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (3) 1/2 - 5/10")

    def test_update_args(self):
        """Test updating Rectangle's attributes using args."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(5, 5, 5, 5, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 5/5 - 5/5")

    def test_update_kwargs(self):
        """Test updating Rectangle's attributes using kwargs."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=5, width=5, height=5, x=5, y=5)
        self.assertEqual(str(r), "[Rectangle] (5) 5/5 - 5/5")

    def test_to_dictionary(self):
        """Test converting Rectangle to dictionary."""
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.to_dictionary(), {'id': 3, 'width': 5, 'height': 10, 'x': 1, 'y': 2})

if __name__ == '__main__':
    unittest.main()
