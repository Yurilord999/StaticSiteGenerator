import re
from markdown_converter import *
from textnode import *
from htmlnode import * 

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

# Converts a whole Markdown document into a HTMLNode tree 
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_types = [block_to_block_type(block) for block in blocks]
    html_nodes = []

    for i in range(len(blocks)):
        html_nodes.append(ParentNode(block_types[i], text_to_leafs(blocks[i])))

    return ParentNode(("div", html_nodes))    

# Converts a single Markdown block into a list of HTML LeafNodes
def text_to_leafs(text):
    text_nodes = text_to_textnodes(text)
    html_leafs = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return html_leafs
