#!/usr/bin/python3
"""module to test review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """class to test review class"""
    def setUp(self):
        """create r"""
        self.r = Review()

    def test_place_id(self):
        """test place id"""
        self.assertEqual(str, type(self.r.place_id))

    def test_user_id(self):
        """test user id"""
        self.assertEqual(str, type(self.r.user_id))

    def test_text(self):
        """test text"""
        self.assertEqual(str, type(self.r.text))


if __name__ == "__main__":
    unittest.main()
