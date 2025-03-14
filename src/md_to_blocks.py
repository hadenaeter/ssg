import re

def markdown_to_blocks(markdown):
    if not markdown:
        return []

    blocks = re.split(r"\n(\s*)\n", markdown) # there might be spaces between \n
    blocks = list(filter(lambda x: x, list(map(lambda x: x.strip(), blocks))))

    return blocks
