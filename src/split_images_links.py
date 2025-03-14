import re
from extract_md import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    matches = r"\!\[(.*?)\]\((.*?)\)"
    for node in old_nodes:
        text = node.text
        if not extract_markdown_images(text):
            raise ValueError("no image in text")
        else:
            start = 0
            middle = 0
            end = 0
            for i in range(0, len(text)):
                if text[i] == "!":
                    start = i
                elif start and text[i] == "]" and text[i+1] == "(":
                    middle = i
                elif start and middle and text[i] == ")":
                    if re.match(matches, text[start:i + 1]):
                        new_nodes.append(
                            TextNode(text[end + 1 if end > 0 else end:start],
                            TextType.NORMAL)
                        )
                        end = i
                        new_nodes.append(
                                TextNode(
                                    text[start+2:middle],
                                    TextType.IMAGE,
                                    text[middle+2:end]
                                )
                        )
                        start = 0
                        middle = 0
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    matches = r"\[(.*?)\]\((.*?)\)"
    for node in old_nodes:
        text = node.text
        if not extract_markdown_links(text):
            raise ValueError("no link in text")
        else:
            start = 0
            middle = 0
            end = 0
            for i in range(0, len(text)):
                if text[i] == "[":
                    start = i
                elif start and text[i] == "]" and text[i+1] == "(":
                    middle = i
                elif start and middle and text[i] == ")":
                    if re.match(matches, text[start:i + 1]):
                        new_nodes.append(
                            TextNode(text[end + 1 if end > 0 else end:start],
                            TextType.NORMAL)
                        )
                        end = i
                        new_nodes.append(
                                TextNode(
                                    text[start+1:middle],
                                    TextType.LINK,
                                    text[middle+2:end]
                                )
                        )
                        start = 0
                        middle = 0
    return new_nodes

"""
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
"""
