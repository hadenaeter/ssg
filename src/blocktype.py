import re
from enum import Enum

class BlockType(Enum):
    """Represents the possible types of markdown text blocks"""
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE_BLOCK = "CODE_BLOCK"
    BLOCKQUOTE = "BLOCKQUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

def block_to_block_type(block):
    if not block:
        return None
    title_match = r"#{1,6} "
    code_block_match = r"`{3}(\s|.)*`{3}"
    blockquote_match = r"^(>.*\n)*$"
    ul_match = r"^(- .*\n)*$"
    ol_match = r"^((\d)*. .*\n)*$"

    if re.match(title_match, block):
        return BlockType.HEADING
    elif re.match(code_block_match, block):
        return BlockType.CODE_BLOCK
    elif re.match(blockquote_match, block + "\n"): # Newline for regex match
        return BlockType.BLOCKQUOTE
    elif re.match(ul_match, block + "\n"):
        return BlockType.UNORDERED_LIST
    elif re.match(ol_match, block + "\n"):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
