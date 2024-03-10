#!/usr/bin/python3
"""test cases"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test the state class"""
    
    def test_name(self):
        """test the name attribute"""
        s = State()
        self.assertEqual(str, type(s.name))

if __name__ == "__main__":
    unittest.main()
