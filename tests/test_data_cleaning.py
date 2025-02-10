import unittest
from src.data_cleaning import clean_data
import logging

#configure logging
logging.disable(logging.CRITICAL)  # Disables logging output for cleaner test results

class TestDataCleaning(unittest.TestCase):
    def test_clean_data_with_valid_input(self):
        sample_data = {"docs": [{"title": "Book1"}, {"title": "Book2"}, {}]}
        cleaned = clean_data(sample_data)
        self.assertEqual(len(cleaned), 2)
        self.assertEqual(cleaned[0]["title"], "Book1")

    def test_clean_data_with_empty_docs(self):
        sample_data = {"docs": []}
        cleaned = clean_data(sample_data)
        self.assertEqual(cleaned, [])

    def test_clean_data_with_none(self):
        cleaned = clean_data(None)
        self.assertIsNone(cleaned)

if __name__ == "__main__":
    unittest.main()
