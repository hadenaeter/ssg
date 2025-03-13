import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {})
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "test-class"})
        self.assertEqual(parent_node.to_html(), ('<div class="test-class">'
            '<span>child</span></div>'))

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [], {})
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), ("ParentNode is missing "
            "children"))

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node], {})
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode is missing a tag")

if __name__ == "__main__":
    unittest.main()
