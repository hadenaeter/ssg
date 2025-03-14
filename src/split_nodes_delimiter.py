from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if (delimiter in text) and (len(text.split(delimiter)) > 2):
            split_node = text.split(delimiter)
            for i in range(0, len(split_node)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_node[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(split_node[i], text_type))
        elif len(text.split(delimiter)) == 2:
            raise Exception("no matching closing delimiter found")
        else:
            new_nodes.append(node)

    return new_nodes
