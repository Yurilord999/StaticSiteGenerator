from textnode import *
from htmlnode import *


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
    text = TextNode("text", "link", "url")
    print(repr(text))
    print(text_node_to_html_node(text))


main()
