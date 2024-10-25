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
    
    def test_split_nodes_link(self):
        node = TextNode("Text with [link 1](https://link.com) and [link 2](https://link2.com)", "text")
        bait = TextNode("Text with [link 1](https://link.com) and ![not link](https://image2.jpeg)", "text")
        links = split_nodes_link([node])
        no_links = split_nodes_link([TextNode("Nothing to split", "text")])
        mix_up = split_nodes_link([bait])
        self.assertListEqual(
            [
                TextNode("Text with ", "text"),
                TextNode("link 1", "link", "https://link.com"),
                TextNode(" and ", "text"),
                TextNode("link 2", "link", "https://link2.com"), 
            ],
            links
        )
        self.assertListEqual([TextNode("Nothing to split", "text")], no_links)
        self.assertListEqual(
            [
                TextNode("Text with ", "text"),
                TextNode("link 1", "link", "https://link.com"),
                TextNode(" and ![not link](https://image2.jpeg)", "text"),            
            ],
            mix_up
        )

    def test_split_nodes_image(self):
        node = TextNode("Text with ![image 1](https://image.gif) and ![image 2](https://image2.jpeg)", "text")
        bait = TextNode("Text with ![image 1](https://image.gif) and [not image](https://image2.jpeg)", "text")
        images = split_nodes_image([node])
        no_images = split_nodes_image([TextNode("Nothing to split", "text")])
        mix_up = split_nodes_image([bait])
        self.assertListEqual(
            [
                TextNode("Text with ", "text"),
                TextNode("image 1", "image", "https://image.gif"),
                TextNode(" and ", "text"),
                TextNode("image 2", "image", "https://image2.jpeg"), 
            ],
            images
        )
        self.assertListEqual([TextNode("Nothing to split", "text")], no_images)
        self.assertListEqual(
            [
                TextNode("Text with ", "text"),
                TextNode("image 1", "image", "https://image.gif"),
                TextNode(" and [not image](https://image2.jpeg)", "text"),            
            ],
            mix_up
        )  

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://image.jpeg) and a [link](https://link.com)" 
        check = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://image.jpeg"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://link.com"),   
            ],
            check
        )     

if __name__ == "__main__":
    unittest.main() 