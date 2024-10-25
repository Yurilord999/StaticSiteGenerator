import unittest
from split_inlines import *
from textnode import *

class TestSplitInline(unittest.TestCase):
    def test_bold(self):
        node = TextNode("text with **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("bold", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )
    
    def test_italic(self):
        node = TextNode("text with *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )
    
    def test_code(self):
        node = TextNode("text with `code` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("text with ", "text"),
                TextNode("code", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_multi(self):
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
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main() 