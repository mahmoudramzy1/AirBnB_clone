#!/usr/bin/python3
"""module for city class"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""

    state_id = ""
    name = ""
