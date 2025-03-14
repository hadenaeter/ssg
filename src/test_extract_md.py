import unittest
from extract_md import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Regular image markdown
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        # Multiple images
        matches = extract_markdown_images(
            "Images: ![First](https://i.imgur.com/first.png) and ![Second](https://i.imgur.com/second.png)"
        )
        self.assertListEqual(
            [("First", "https://i.imgur.com/first.png"), ("Second", "https://i.imgur.com/second.png")],
            matches
        )

        # No images
        matches = extract_markdown_images("This is a text without images.")
        self.assertListEqual([], matches)

        # Malformed image markdown
        matches = extract_markdown_images("This is malformed ![image](https://img.com/image without closing parenthesis")
        self.assertListEqual([], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        # Regular link markdown
        matches = extract_markdown_links(
            "This is a link to [Google](https://www.google.com)"
        )
        self.assertListEqual([("Google", "https://www.google.com")], matches)

        # Multiple links
        matches = extract_markdown_links(
            "Links: [Google](https://www.google.com) and [OpenAI](https://www.openai.com)"
        )
        self.assertListEqual(
            [("Google", "https://www.google.com"), ("OpenAI", "https://www.openai.com")],
            matches
        )

        # No links
        matches = extract_markdown_links("This is a text without links.")
        self.assertListEqual([], matches)

        # Malformed link markdown
        matches = extract_markdown_links("This is malformed [link](https://link without closing parenthesis")
        self.assertListEqual([], matches)

        # Links with different formatting
        matches = extract_markdown_links("[Link with spaces](https://example.com/some path) and [Another Link](https://example.com/another)")
        self.assertListEqual(
            [("Link with spaces", "https://example.com/some path"), ("Another Link", "https://example.com/another")],
            matches
        )

if __name__ == '__main__':
    unittest.main()
