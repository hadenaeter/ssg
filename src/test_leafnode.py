import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "This is a paragraph").to_html()
        self.assertEqual(
            node,
            "<p>This is a paragraph</p>"
        )

        node = LeafNode(
            "p",
            "This is a big blue paragraph",
            {"id": "bb", "class": "big blue"}
        ).to_html()
        self.assertEqual(
            node,
            '<p id="bb" class="big blue">This is a big blue paragraph</p>'
        )

    def test_empty_value(self):
        node = LeafNode("p", "").to_html()
        self.assertEqual(node, "<p></p>")

    def test_missing_tag(self):
        node = LeafNode(None, "No tag here").to_html()
        self.assertEqual(
            node,
            "No tag here"
        )

    def test_custom_attributes(self):
        props = {"data-test": "value", "style": "color: red;"}
        node = LeafNode("div", "Hello", props).to_html()
        self.assertEqual(
            node,
            '<div data-test="value" style="color: red;">Hello</div>'
        )
