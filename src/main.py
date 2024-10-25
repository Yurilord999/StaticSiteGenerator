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

    #print(node.to_html())
    #print(repr(node2))
    node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
    test = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(test))
    #test1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(test1))
    #test2 = "This is text with a link to boot"
    #print(extract_markdown_links(test2))
    #test4 = split_nodes_image(test2)
    #print(test4)
    #print(node)
    split = split_nodes_link([TextNode("Text with [link 1](https://link.com) and ![not link](https://image2.jpeg)", "text")])
    print(split)


main()
