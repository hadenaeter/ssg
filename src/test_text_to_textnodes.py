import unittest
from text_to_textnodes import text_to_text_nodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_normal(self):
        text = ("This is **text** with an _italic_ word and a `code block` and "
        "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link]"
        "(https://boot.dev)")
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_normal_text(self):
            text = "This is just normal text."
            converted = text_to_text_nodes(text)
            self.assertEqual(
                converted,
                [TextNode("This is just normal text.", TextType.NORMAL)]
            )

    def test_bold_text(self):
        text = "This is **bold** text."
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [TextNode("This is ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.NORMAL)]
        )

    def test_italic_text(self):
        text = "This is _italic_ text."
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [TextNode("This is ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.NORMAL)]
        )

    def test_code_text(self):
        text = "This is `code`."
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [TextNode("This is ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(".", TextType.NORMAL)]
        )

    def test_mixed_formatting(self):
        text = "This is **bold** and _italic_ text with a `code`."
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [TextNode("This is ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text with a ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(".", TextType.NORMAL)]
        )

    def test_images_and_links(self):
        text = "An image: ![image](https://example.com/image.png) and a link: [link](https://example.com)"
        converted = text_to_text_nodes(text)
        self.assertEqual(
            converted,
            [TextNode("An image: ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" and a link: ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://example.com")]
        )

    def test_empty_string(self):
        text = ""
        converted = text_to_text_nodes(text)
        self.assertEqual(converted, [])

    if __name__ == "__main__":
        unittest.main()
