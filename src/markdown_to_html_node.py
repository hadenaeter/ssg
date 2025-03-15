from md_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from parentnode import ParentNode
from text_to_textnodes import text_to_text_nodes
from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                block = block.replace("\n", " ").strip()
                html_nodes.append(ParentNode(
                    "p",
                    text_to_children(block)
                ))
            case BlockType.HEADING:
                block = block.replace("\n", " ")
                heading_level = get_heading_level(block)
                html_nodes.append(ParentNode(
                    f"h{heading_level}",
                    text_to_children(block.replace("# ", "").replace("#", ""))
                ))
            case BlockType.CODE_BLOCK:
                block = (block + "\n").replace("```\n", "")
                html_nodes.append(ParentNode(
                    "pre",
                    [ParentNode(
                        "code",
                        [LeafNode(None, block)]
                    )]
                ))
            case BlockType.BLOCKQUOTE:
                block = block.replace('\n', '')[2:].replace(
                    ('>' or '> '),
                    '<br>'
                )
                html_nodes.append(ParentNode(
                    "blockquote",
                    text_to_children(block)
                ))
            case BlockType.UNORDERED_LIST:
                html_nodes.append(ParentNode(
                    "ul",
                    text_to_children(block, lst = "ul")
                ))
            case BlockType.ORDERED_LIST:
                html_nodes.append(ParentNode(
                    "ol",
                    text_to_children(block, lst = "ol")
                ))
    parent_node = ParentNode(
        "div",
        [node for node in html_nodes]
    )
    return parent_node

def text_to_children(block, lst = None):
    if not lst:
        text_nodes = text_to_text_nodes(block)
        html_nodes = list(map(text_node_to_html_node, text_nodes))
    else:
        list_items = block.split("\n")
        if lst == "ul":
            html_nodes = list(map(
                lambda item: ParentNode(
                    "li",
                    list(map(text_node_to_html_node, text_to_text_nodes(item[2:])))
                ),
                list_items
            ))
        elif lst == "ol":
            html_nodes = []
            for i in range(0, len(list_items)):
                html_nodes.append(
                    ParentNode(
                        "li",
                        list(map(
                            text_node_to_html_node,
                            text_to_text_nodes(list_items[i][len(str(i+1)) + 2:])
                        ))
                    )
                )
        else:
            raise ValueError("Invalid lst value( accepts'ul' or 'ol' only)")

    return [node for node in html_nodes]

def get_heading_level(block):
    level = 1
    for i in range(1, len(block)):
        if block[i] == " ":
            return level
        elif block[i] == "#":
            level += 1
    return level
