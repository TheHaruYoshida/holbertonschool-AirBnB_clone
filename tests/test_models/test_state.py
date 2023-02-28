#!/usr/bin/python3
"""test State class"""

import unittest
import models
import datetime


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_dummy(self):
        """Dummy test to avoid unittest errors"""
        pass

    def test_documentation(self):
        """Tests if module, class and methods have documentation"""
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(models.state.State.__doc__)

    def test_instance(self):
        """Tests if object created is an instance of State class"""
        instance = models.state.State()
        self.assertIsInstance(instance, models.state.State)

    def test_attribute_types(self):
        """Tests if all instance attributes have correct types"""
        instance = models.state.State()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()

