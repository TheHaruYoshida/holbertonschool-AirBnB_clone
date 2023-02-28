#!/usr/bin/python3
"""test Review class"""

import unittest
import models
import datetime


class TestReviewClass(unittest.TestCase):
    """Test Review class"""

    def test_nothing(self):
        """test for method that does nothing"""
        pass

    def test_documentation(self):
        """test module and class docstring"""
        self.assertIsNotNone(models.review.__doc__)
        self.assertIsNotNone(models.review.Review.__doc__)

    def test_instance_class(self):
        """test instance class"""
        instance = models.review.Review()
        self.assertIsInstance(instance, models.review.Review)

    def test_attribute_types(self):
        """test types of instance attributes"""
        instance = models.review.Review()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)


if __name__ == "__main__":
    unittest.main()

