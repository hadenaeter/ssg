import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("### Heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```code block```"), BlockType.CODE_BLOCK)

    def test_blockquote(self):
        self.assertEqual(block_to_block_type("> This is a blockquote."), BlockType.BLOCKQUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a paragraph."), BlockType.PARAGRAPH)

    def test_long_paragraph(self):
        long_paragraph = "This is a long paragraph designed to test the block_to_block_type function. " \
                         "It contains multiple sentences, ensuring that the function can handle " \
                         "more extensive text inputs without issue."
        self.assertEqual(block_to_block_type(long_paragraph), BlockType.PARAGRAPH)

    def test_empty_paragraph(self):
        self.assertEqual(block_to_block_type(""), None)

    def test_multiple_paragraphs(self):
        multiple_paragraphs = "This is the first paragraph.\n\nThis is the second paragraph."
        self.assertEqual(block_to_block_type(multiple_paragraphs), BlockType.PARAGRAPH)

    def test_long_heading(self):
        long_heading = "#" + " H" * 100
        self.assertEqual(block_to_block_type(long_heading), BlockType.HEADING)

    def test_long_code_block(self):
        long_code_block = "```" + "\n" + "\n".join("print('This is line " + str(i) + "')" for i in range(1, 101)) + "\n```"
        self.assertEqual(block_to_block_type(long_code_block), BlockType.CODE_BLOCK)

    def test_long_blockquote(self):
        long_blockquote = "> " + "This is a very long blockquote that spans multiple sentences. " * 10
        self.assertEqual(block_to_block_type(long_blockquote.strip()), BlockType.BLOCKQUOTE)

    def test_long_unordered_list(self):
        long_unordered_list = "\n".join("- Item " + str(i) for i in range(1, 101))
        self.assertEqual(block_to_block_type(long_unordered_list), BlockType.UNORDERED_LIST)

    def test_long_ordered_list(self):
        long_ordered_list = "\n".join(str(i) + ". Item " + str(i) for i in range(1, 101))
        self.assertEqual(block_to_block_type(long_ordered_list), BlockType.ORDERED_LIST)

    def test_long_multiple_paragraphs(self):
        long_multiple_paragraphs = "\n\n".join("This is paragraph " + str(i) + "." for i in range(1, 11))
        self.assertEqual(block_to_block_type(long_multiple_paragraphs), BlockType.PARAGRAPH)
