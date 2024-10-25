from textnode import *
""" 
Converting raw Markdown string into list of multiple nodes based on delimiter:
Currently it only works with text first->markdown->text !
Example:

"Text with a **bolded phrase** in the middle" ->
[
    TextNode("Text with a ", "text"),
    TextNode("bolded phrase", "bold"),
    TextNode(" in the middle", "text"),
]
"""

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # only split TextType.TEXT, append others as is
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