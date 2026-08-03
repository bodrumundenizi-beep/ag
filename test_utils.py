"""
Basic unit tests for the utility functions.
"""

import unittest
from utils import clean_text, calculate_stats

class TestUtils(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("  hello   world  "), "Hello world")
        self.assertEqual(clean_text("python programming"), "Python programming")
        self.assertEqual(clean_text(""), "")

    def test_calculate_stats(self):
        result = calculate_stats([10, 20, 30])
        self.assertEqual(result["count"], 3)
        self.assertEqual(result["average"], 20.0)
        self.assertEqual(result["max"], 30)
        self.assertEqual(result["min"], 10)

        empty_result = calculate_stats([])
        self.assertEqual(empty_result["count"], 0)

if __name__ == "__main__":
    unittest.main()
