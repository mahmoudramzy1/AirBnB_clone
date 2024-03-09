#!/usr/bin/python3
"""test for user module"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing the user class"""
    
    def SetUp(self):
        """create my user"""
        cls.my = User()


    def test_attributes(self):
        """test the attributes"""
        user5 = User(email="mahmoud@gmail.com")
        user5.password = 123
        user5.first_name = "Jane"
        user5.last_name = "Foster"
        self.assertEqual(user5.email, "mahmoud@gmail.com")
        self.assertEqual(user5.password, 123)
        self.assertEqual(user5.first_name, "Jane")
        self.assertEqual(user5.last_name, "Foster")

