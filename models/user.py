#!/usr/bin/python3
"""module for user class"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """class defines users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
