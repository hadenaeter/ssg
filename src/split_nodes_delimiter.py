from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        # if the length of the sections after splitting the text is not even,
        # then there was an even number of instances of delimiter, which means
        # that every delimeter was closed properly, at least for our purposes.
        if (delimiter in text) and (len(text.split(delimiter)) % 2 != 0):
            split_node = text.split(delimiter)
            for i in range(0, len(split_node)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_node[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(split_node[i], text_type))
        # else if the length of the sections after splitting is even, there was
        # an odd number of instances of delimiter, meaning there was a delimiter
        # which was not closed properly.
        elif len(text.split(delimiter)) % 2 == 0:
            raise Exception("no matching closing delimiter found")
        else:
            new_nodes.append(node)

    return new_nodes
