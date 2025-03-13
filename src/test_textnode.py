import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):

    def test_text_node_equality(self):
        node1 = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("Hello", TextType.NORMAL)
        node3 = TextNode("Hello", TextType.BOLD)

        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    def test_text_node_representation(self):
        node = TextNode("Hello", TextType.NORMAL)
        expected_repr = "TextNode(text='Hello', text_type='NORMAL', url=None)"

        self.assertEqual(repr(node), expected_repr)

    def test_text_node_with_url(self):
        node_with_url = TextNode("Click here",
            TextType.LINK,
            url="https://example.com")
        expected_repr = ("TextNode(text='Click here', text_type='LINK', "
            "url='https://example.com')")

        self.assertEqual(repr(node_with_url), expected_repr)

    def test_text_node_edge_cases(self):
        node1 = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("Hello", TextType.NORMAL, url=None)
        node3 = TextNode("Hello", TextType.BOLD, url=None)
        node4 = TextNode("Hello", TextType.NORMAL, url="https://example.com")

        # Test equality when URL is None but text type is different
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

        # Test representation with URL as None
        expected_repr_node2 = ("TextNode(text='Hello', text_type='NORMAL', "
            "url=None)")
        self.assertEqual(repr(node2), expected_repr_node2)

        # Test representation with a valid URL
        expected_repr_node4 = ("TextNode(text='Hello', text_type='NORMAL', "
            "url='https://example.com')")
        self.assertEqual(repr(node4), expected_repr_node4)

if __name__ == "__main__":
    unittest.main()
