import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

        def test_props_to_html_one_prop(self):
            node = HTMLNode(tag='input', props={'type': 'text'})
            self.assertEqual(node.props_to_html(), ' type="text"')

        def test_props_to_html_multiple_props(self):
            node = HTMLNode(tag='a', props={'href': 'http://example.com', 'target': '_blank'})
            self.assertEqual(node.props_to_html(), ' href="http://example.com" target="_blank"')

        def test_children_rendering(self):
            child_node = HTMLNode(tag='span', value='Child')
            node = HTMLNode(tag='div', children=[child_node])
            self.assertEqual(repr(node.children[0]), repr(child_node))

        def test_nested_children(self):
            child_node = HTMLNode(tag='span', value='Child')
            child_node2 = HTMLNode(tag='a', children=[HTMLNode(value='Link')])
            parent_node = HTMLNode(tag='div', children=[child_node, child_node2])
            self.assertEqual(len(parent_node.children), 2)

        def test_empty_node(self):
            node = HTMLNode()
            self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=[], props={})")

        def test_node_with_tag_only(self):
            node = HTMLNode(tag='div')
            self.assertEqual(repr(node), "HTMLNode(tag='div', value=None, children=[], props={})")

        def test_node_with_value(self):
            node = HTMLNode(value="Hello World")
            self.assertEqual(repr(node), "HTMLNode(tag=None, value='Hello World', children=[], props={})")

        def test_node_with_children(self):
            child_node = HTMLNode(tag='span', value='Click Me')
            node = HTMLNode(tag='button', children=[child_node])
            self.assertEqual(repr(node), "HTMLNode(tag='button', value=None, children=[HTMLNode(tag='span', value='Click Me', children=[], props={})], props={})")

        def test_node_with_props(self):
            node = HTMLNode(tag='input', props={'type': 'text', 'placeholder': 'Enter text'})
            self.assertEqual(repr(node), "HTMLNode(tag='input', value=None, children=[], props={'type': 'text', 'placeholder': 'Enter text'})")

        def test_node_with_all_properties(self):
            node = HTMLNode(tag='a', value='Link', props={'href': 'http://example.com'},
                            children=[HTMLNode(tag='span', value='span text')])
            self.assertEqual(repr(node), "HTMLNode(tag='a', value='Link', children=[HTMLNode(tag='span', value='span text', children=[], props={})], props={'href': 'http://example.com'})")
