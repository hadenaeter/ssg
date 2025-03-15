import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_bold_and_italic(self):
        md = """
This is a paragraph with **bold** and _italic_ text.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>",
        )

    def test_link(self):
        md = """
This is a link to [OpenAI](https://openai.com).
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a link to <a href=\"https://openai.com\">OpenAI</a>.</p></div>",
        )

    def test_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

# Test blockquotes
    def test_blockquote(self):
        md = """
> This is a blockquote.
> It spans multiple lines.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote.<br>It spans multiple lines.</blockquote></div>",
        )

# Test ordered lists
    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

# Test headings
    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

# Test paragraphs and code blocks again for emphasis
    def test_paragraphs_and_codeblocks(self):
        md = """
This is a regular paragraph.

```
This is another code block.
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a regular paragraph.</p><pre><code>This is another code block.\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
