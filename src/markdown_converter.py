from textnode import *
import re
""" 
Converting raw Markdown string into a list of multiple nodes based on delimiter:
Currently it only works with text first->markdown->text !
Example:

"Text with a **bolded phrase** in the middle" ->
[
    TextNode("Text with a ", "text"),
    TextNode("bolded phrase", "bold"),
    TextNode(" in the middle", "text"),
]
"""

# convert markdown to a TextNode, then converting into a list of TextNodes of their respective type
def text_to_textnodes(text):
        new_nodes = [TextNode(text, "text")]
        new_nodes = split_nodes_delimiter(new_nodes, "`", "code")
        new_nodes = split_nodes_delimiter(new_nodes, "**", "bold")
        new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
        new_nodes = split_nodes_image(new_nodes)
        new_nodes = split_nodes_link(new_nodes)
        return new_nodes

# see top description   
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # only split text_type_text, append others as is
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        # check for proper syntax (closing delimiter)
        splitted = node.text.split(delimiter)
        check = 0
        for letter in splitted:
            if letter == delimiter:
                check +=1
        if check % 2 != 0:
            raise Exception("Invalid Markdown syntax. No closing delimiter")
        
        # return sliced nodes
        node_sections = []
        for i in range(len(splitted)):
            if splitted[i] == "":
                continue
            if i%2 == 0:
                node_sections.append(TextNode(splitted[i],"text"))
            else:
                node_sections.append(TextNode(splitted[i],text_type))
        new_nodes.extend(node_sections)
    return new_nodes

# image = delimiter
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        remaining_text = node.text
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue

        node_sections = []
        for alt, link in images:
            splitted = remaining_text.split(f"![{alt}]({link})", 1)
            if splitted[0] == "":
                continue
            node_sections.append(TextNode(splitted[0],"text"))
            node_sections.append(TextNode(alt, "image" ,link))
            if len(splitted) > 1:
                remaining_text = splitted[1]

        if remaining_text:
            node_sections.append(TextNode(remaining_text, "text"))

        new_nodes.extend(node_sections)
    return new_nodes

# link = delimiter
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        remaining_text = node.text
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue

        node_sections = []
        for des, link in links:
            splitted = remaining_text.split(f"[{des}]({link})", 1)
            if splitted[0] == "":
                continue
            node_sections.append(TextNode(splitted[0],"text"))
            node_sections.append(TextNode(des, "link" ,link))
            if len(splitted) > 1:
                remaining_text = splitted[1]
            
        if remaining_text:
            node_sections.append(TextNode(remaining_text, "text"))

        new_nodes.extend(node_sections)
    return new_nodes

# extracts alt & link from markdown text as a tuple in a list
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# extracts description & link from markdown text as a tuple in a list
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)



