from enum import Enum

class TextType(Enum):
    """Represents the possible types of inline markdown text"""
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

class TextNode:
    """
    Represents a text node that contains text content, its formatting type, and
    an optional URL (used for links and images).
    """
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Determines if two TextNodes are equal by comparing their text, text
        type, and optional URL.
        """
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url)

    def __repr__(self):
        """
        Returns a string representation of the TextNode, displaying its text,
        text type, and URL (if applicable), useful for debugging.
        """
        return (f"TextNode(text={self.text!r}, "
            f"text_type={self.text_type.value!r}, url={self.url!r})")

    # Example Usage of the TextNode class:
    # node = TextNode("This is some text.", TextType.NORMAL)
    # node2 = TextNode("click here", TextType.LINK, "www.example.com")
