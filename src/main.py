from textnode import *
from htmlnode import *
from markdown_converter import *


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
    test = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(test))
    test1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(test1))
    

main()
