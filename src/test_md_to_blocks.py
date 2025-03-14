import unittest
from md_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_functionality(self):
        markdown = (
            "\n\n\n\n\n\n"
            "\n\n              \n\n      \n\n"
            "# This is a heading\n\nThis is a paragraph of text. It has some "
            "**bold** and _italic_ words inside of it.\n\n- This is the first list" " item in a list block\n- This is a list item\n- This is another list"
            " item"
            "\n\n\n\n\n"
        )
        converted = markdown_to_blocks(markdown)
        self.assertEqual(
            converted,
            [
                "# This is a heading", "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ]
        )

    def test_empty_input(self):
        self.assertEqual(markdown_to_blocks(""), [])
        self.assertEqual(markdown_to_blocks(None), [])

    def test_whitespace_only(self):
        self.assertEqual(markdown_to_blocks("   \n\n\t\n\n  "), [])

    def test_single_block(self):
        markdown = "# This is a heading\nThis is a single block."
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading\nThis is a single block."])

    def test_multiple_blocks_with_whitespace(self):
        markdown = "# Block 1\n\n\n   \n\n  - Item 1\n   \n- Item 2    \n\n\n\n"
        self.assertEqual(markdown_to_blocks(markdown), ["# Block 1", "- Item 1", "- Item 2"])

    def test_blocks_with_only_markdown_syntax(self):
            markdown = "# Heading 1\n\n* List Item 1\n* List Item 2"
            self.assertEqual(markdown_to_blocks(markdown), ["# Heading 1", "* List Item 1\n* List Item 2"])
