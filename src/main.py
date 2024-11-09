from textnode import *
from htmlnode import *
from markdown_converter import *
from markdown_blocks import *


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


    node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    split = split_nodes_link([TextNode("Text with [link 1](https://link.com) and ![not link](https://image2.jpeg)", "text")])

    
    markdown = """#### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    converted = markdown_to_html_node(markdown)
    print(converted.to_html())
    print("------------------")

    markdown = """
- list *italic*
- list `code`
- dsdsdsd


1. **law**
2. and order

"""

    converted = markdown_to_html_node(markdown)
    print(converted.to_html())


main()
