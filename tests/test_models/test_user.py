#!/usr/bin/python3
"""test for user module"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing the user class"""
    
    def SetUp(self):
        """create my user"""
        cls.u = User()


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
    
     def test_email(self):
        """test email"""
        self.assertEqual(str, type(self.u.email))

    def test_password(self):
        """test password"""
        self.assertEqual(str, type(self.u.password))

    def test_first_name(self):
        """test first name"""
        self.assertEqual(str, type(self.u.first_name))

    def test_last_name(self):
        """test second name"""
        self.assertEqual(str, type(self.u.last_name))

