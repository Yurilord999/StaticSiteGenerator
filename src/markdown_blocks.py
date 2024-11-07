# split block markdown text into segements -> list
def markdown_to_blocks(markdown_string):
    blocks = markdown_string.split("\n\n")
    blocks = [block.strip() for block in blocks]
    clean_blocks = [block for block in blocks if block != ""]
    return clean_blocks 