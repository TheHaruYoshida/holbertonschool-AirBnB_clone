#!/usr/bin/phython3
"""Amenity"""


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
