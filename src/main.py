from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

def main():
    old_nodes = [
        TextNode("This is text with a `code block` word.", TextType.NORMAL),
        TextNode("This is **bold text** right here.", TextType.NORMAL),
        TextNode("Did someone say _italic_?", TextType.NORMAL),
    ]

    new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

    print(new_nodes)

if __name__=="__main__":
    main()
