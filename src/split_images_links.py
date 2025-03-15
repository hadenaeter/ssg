import re
from extract_md import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    matches = r"\!\[(.*?)\]\((.*?)\)"
    for node in old_nodes:
        text = node.text
        start = -1
        middle = 0
        end = 0
        if not extract_markdown_images(text):
            new_nodes.append(node)
        else:
            for i in range(0, len(text)):
                if text[i] == "!":
                    start = i
                elif start >= 0 and text[i] == "]" and text[i+1] == "(":
                    middle = i
                elif start >= 0 and middle and text[i] == ")":
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
                        start = -1
                        middle = 0

            if not (end == len(text) - 1):
                new_nodes.append(
                    TextNode(text[end+1:], TextType.NORMAL)
                )
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    matches = r"\[(.*?)\]\((.*?)\)"
    start = -1
    middle = 0
    end = 0
    for node in old_nodes:
        text = node.text
        if not extract_markdown_links(text):
            new_nodes.append(node)
        else:
            for i in range(0, len(text)):
                if text[i] == "[":
                    start = i
                elif start >= 0 and text[i] == "]" and text[i+1] == "(":
                    middle = i
                elif start >= 0 and middle and text[i] == ")":
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
            if not (end == len(text) - 1):
                new_nodes.append(
                    TextNode(text[end+1:], TextType.NORMAL)
                )
    return new_nodes
