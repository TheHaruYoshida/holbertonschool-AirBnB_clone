"""Test module for BaseModel class"""

import unittest
import models
import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel class"""

    def test_dummy(self):
        """Dummy test case to prevent unittest from failing"""
        pass

    def test_documentation(self):
        """Tests for module and method documentation"""
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__)
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__)

    def test_instance(self):
        """Test instance creation of BaseModel"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance, models.base_model.BaseModel)

    def test_attribute_types(self):
        """Test attribute types of BaseModel instance"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_attribute_initialization(self):
        """Test attribute initialization of BaseModel instance"""
        instance = models.base_model.BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_str_method(self):
        """Test __str__ method of BaseModel instance"""
        instance = models.base_model.BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_string, str(instance))

    def test_save_method(self):
        """Test save method of BaseModel instance"""
        instance = models.base_model.BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertLess(original_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel instance"""
        instance = models.base_model.BaseModel()
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(instance.__class__.__name__, dictionary["__class__"])
        self.assertEqual(instance.id, dictionary["id"])


if __name__ == "__main__":
    unittest.main()

