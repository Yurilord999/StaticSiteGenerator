import re

# split block markdown text into segements -> list
def markdown_to_blocks(markdown_string):
    blocks = markdown_string.split("\n\n")
    blocks = [block.strip() for block in blocks]
    clean_blocks = [block for block in blocks if block != ""]
    return clean_blocks 

# takes a single block of markdown and returns its type -> String
def block_to_block_type(markdown_block):
    if re.match(r"^#{1,6}[\s]", markdown_block):
        return "heading"
    elif re.fullmatch(r"^```.*```$", markdown_block, re.DOTALL):
        return "code"
    elif re.fullmatch(r"^(>.*\n?)*$", markdown_block, flags = re.MULTILINE):
        return "quote"
    elif re.fullmatch(r"^([*-] .*\n?)*$", markdown_block, flags = re.MULTILINE):
        return "unordered_list"
    elif re.fullmatch(r"^((\d+)\. .*\n?)*$", markdown_block, flags = re.MULTILINE):
        lines = markdown_block.splitlines()
        tracker = 1
        for line in lines:
            match = re.match(r"^(\d+)\. .*$", line)
            line_number = int(match.group(1))
            if line_number == tracker:
                tracker += 1
            else:
                return "paragraph"
        return "ordered_list"
    return "paragraph"
