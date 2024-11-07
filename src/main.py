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


    node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    split = split_nodes_link([TextNode("Text with [link 1](https://link.com) and ![not link](https://image2.jpeg)", "text")])
    print(text_to_textnodes(text))

    markdown_string = "# This is a heading\n\n\n\n\n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item"

    print(markdown_to_blocks(markdown_string))


main()
