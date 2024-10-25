from textnode import *
from htmlnode import *
from split_inlines import *


def main():

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    node2 = ParentNode("a", [LeafNode("b", "Bold text")], {"href": "url"})

    print(node.to_html())
    print(repr(node2))
    text = TextNode("text123 `code` rererer", "text")
    #print(repr(text))
    #print(text_node_to_html_node(text))
    split = split_nodes_delimiter([text], "`", "code")
    print(split)


main()
