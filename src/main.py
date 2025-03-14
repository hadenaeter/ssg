import unittest
from split_images_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png" ")and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.NORMAL,
    )
new_nodes = split_nodes_image([node])
for node in new_nodes:
    print(node)

print("============")

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL,
)
new_nodes = split_nodes_link([node])
for node in new_nodes:
    print(node)


def main():
    pass

if __name__=="__main__":
    main()
