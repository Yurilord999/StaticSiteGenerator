import unittest
from markdown_converter import *
from textnode import *

class TestMarkdown(unittest.TestCase):
    def test_markdown_bold(self):
        node = TextNode("text with **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("bold", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes
        )
    
    def test_markdown_talic(self):
        node = TextNode("text with *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes
        )
    
    def test_markdown_code(self):
        node = TextNode("text with `code` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("code", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes
        )

    def test_markdown_multi(self):
        node = TextNode("text with `code words` and **bold words** and *italic words*", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        new_nodes = split_nodes_delimiter(new_nodes, "**", "bold")
        new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("code words", "code"),
                TextNode(" and ", "text"),
                TextNode("bold words", "bold"),
                TextNode(" and ", "text"),
                TextNode("italic words", "italic"),
            ],
            new_nodes
        )
    
    def test_markdown_images(self):
        text = "Text with ![image1](https://image.jpeg) and ![image2](https://image.gif)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image1", "https://image.jpeg"), 
                ("image2", "https://image.gif")
            ], 
            images
        )

    def test_markdown_links(self):
        text = "Text with [link1](https://link.com) and [link2](https://link2.com)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link1", "https://link.com"),
                ("link2", "https://link2.com")
            ], 
            links
        )


if __name__ == "__main__":
    unittest.main() 