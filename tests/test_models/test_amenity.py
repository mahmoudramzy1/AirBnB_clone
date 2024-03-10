#!/usr/bin/python3
"""module to test amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test amenity"""

    def test_name(self):
        """test name attribute"""
        a = Amenity()
        self.assertEquale(str, type(a.name))

if __name__ = "__main__":
    unittest.main()
