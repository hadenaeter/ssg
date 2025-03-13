from nodes.textnode import TextNode, TextType

def main():
    node = TextNode("Click here", TextType.LINK, url="https://example.com")
    print(node)

if __name__=="__main__":
    main()
