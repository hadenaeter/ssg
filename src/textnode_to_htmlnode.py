from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(
                None,
                text_node.text,
            )
        case TextType.BOLD:
            return LeafNode(
                "b",
                text_node.text
            )
        case TextType.ITALIC:
            return LeafNode(
                "i",
                text_node.text
            )
        case TextType.CODE:
            return LeafNode(
                "code",
                text_node.text
            )
        case TextType.LINK:
            return LeafNode(
                "a",
                text_node.text,
                {"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                "img",
                "",
                {"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise TypeError("TextNode is not a type of TextType")
