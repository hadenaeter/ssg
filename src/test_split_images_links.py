import unittest
from split_images_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestSplitNodesImage(unittest.TestCase):
    def test_normal(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.NORMAL,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.NORMAL),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.NORMAL),
                    TextNode(
                        "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                    ),
                ],
                new_nodes,
            )

    def test_no_images(self):
        node = TextNode(
            "This is text without any images.",
            TextType.NORMAL,
        )
        with self.assertRaises(ValueError) as context:
            split_nodes_image([node])
        self.assertEqual(str(context.exception), "no image in text")

    def test_broken_syntax(self):
        node = TextNode(
            "This is a broken ![image](https://i.imgur.com/zjjcJKZ.png and some regular text.",
            TextType.NORMAL,
        )
        with self.assertRaises(ValueError) as context:
            split_nodes_image([node])
        self.assertEqual(str(context.exception), "no image in text")

    def test_concatenated_images(self):
        node = TextNode(
            "This is text with images ![img1](url1)![img2](url2)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with images ", TextType.NORMAL),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("", TextType.NORMAL),  # Empty text between two images
                TextNode("img2", TextType.IMAGE, "url2")
            ],
            new_nodes,
        )

class TestSplitNodesLink(unittest.TestCase):
    def test_normal(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.LINK,
                    "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )

        def test_no_links(self):
                node = TextNode(
                    "This is text without any links.",
                    TextType.NORMAL,
                )
                with self.assertRaises(ValueError) as context:
                    split_nodes_link([node])
                self.assertEqual(str(context.exception), "no link in text")

        def test_broken_syntax(self):
            node = TextNode(
                "This is a broken [link](https://www.boot.dev and some regular text.",
                TextType.NORMAL,
            )
            with self.assertRaises(ValueError) as context:
                split_nodes_link([node])
            self.assertEqual(str(context.exception), "no link in text")

        def test_concatenated_links(self):
            node = TextNode(
                "This is text with links [link1](url1)[link2](url2)",
                TextType.NORMAL,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with links ", TextType.NORMAL),
                    TextNode("link1", TextType.LINK, "url1"),
                    TextNode("", TextType.NORMAL),  # Empty text between two links
                    TextNode("link2", TextType.LINK, "url2")
                ],
                new_nodes,
            )

if __name__ == "__main__":
    unittest.main()
