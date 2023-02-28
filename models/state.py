#!/usr/bin/python3
"""State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
