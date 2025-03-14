from split_nodes_delimiter import split_nodes_delimiter
from split_images_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

def text_to_text_nodes(text):
    if text:
        text_nodes = [TextNode(text, TextType.NORMAL)]
    else:
        return []
    # Bold
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    # Italic
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    # Code
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    # Images
    text_nodes = split_nodes_image(text_nodes)
    # Link
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes
