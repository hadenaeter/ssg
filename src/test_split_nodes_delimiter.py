import unittest
from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_nodes(self):
        old_nodes = [
            TextNode("This is text with a `code block` word.", TextType.NORMAL),
            TextNode("This is **bold text** right here.", TextType.NORMAL),
            TextNode("Did someone say _italic_?", TextType.NORMAL),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word.", TextType.NORMAL),
                TextNode("This is ", TextType.NORMAL),
                TextNode("bold text", TextType.BOLD),
                TextNode(" right here.", TextType.NORMAL),
                TextNode("Did someone say ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode("?", TextType.NORMAL)
            ]
        )
