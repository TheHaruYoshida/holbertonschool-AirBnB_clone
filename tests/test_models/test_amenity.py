#!/usr/bin/python3
""" Test model - Amenity """
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """class for test Amenity."""

    def setUp(self):
        """Set up the test by creating an instance of the Amenity class."""
        self.amenity = Amenity()
        self.amenity.name = ""

    def test_instance_inheritance(self):
        """Test if an Amenity instance is also an instance of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

    def test_name_attr_existence(self):
        """Test if an Amenity instance has a 'name' attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_name_attr_type(self):
        """Test if the 'name' attribute of an Amenity instance is of type str."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_name_attr_initialization(self):
        """Test if the 'name' attribute of an Amenity instance is initialized to an empty string """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
