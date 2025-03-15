import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extracts_first_level_heading(self):
        markdown = "# Title\nSome content here."
        self.assertEqual(extract_title(markdown), "Title")

    def test_no_heading(self):
        markdown = "Some content here without a heading."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No title (level 1 heading, e.g.'# title') found")

    def test_multiple_headings(self):
        markdown = "# First Title\n# Second Title\nContent here."
        self.assertEqual(extract_title(markdown), "First Title")
