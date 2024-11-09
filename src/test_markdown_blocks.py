import unittest
from markdown_blocks import *

class TestMarkdown_Blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_markdown_to_blocks_remove_empty_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. 


It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text.",
                "It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_block_to_block_types(self):
        heading = "# heading"
        heading2 = "###### heading"
        no_heading = "#no_heading"
        no_heading2 = "############# no_heading"
        self.assertEqual(block_to_block_type(heading), "heading")
        self.assertEqual(block_to_block_type(heading2), "heading")
        self.assertNotEqual(block_to_block_type(no_heading), "heading")
        self.assertNotEqual(block_to_block_type(no_heading2), "heading")

        code = "```code\ncode\ncode```"
        no_code = "``no_code``"
        self.assertEqual(block_to_block_type(code), "code")
        self.assertNotEqual(block_to_block_type(no_code), "code")

        quote = ">quote\n>quote\n>quote"
        no_quote = ">no_quote\nno_quote\n>no_quote"
        self.assertEqual(block_to_block_type(quote), "quote")
        self.assertNotEqual(block_to_block_type(no_quote), "quote")

        u_list = "* list\n- list\n* list"
        no_u_list = "* list\n list\n* list"
        self.assertEqual(block_to_block_type(u_list), "unordered_list")
        self.assertNotEqual(block_to_block_type(no_u_list), "unordered_list")

        o_list = "1. list\n2. list\n3. list"
        no_o_list = "1. list\n3. list\n2. list"
        self.assertEqual(block_to_block_type(o_list), "ordered_list")
        self.assertNotEqual(block_to_block_type(no_o_list), "ordered_list")

        paragraph = "paragraph\n1. paragraph\n>paragraph"
        self.assertEqual(block_to_block_type(paragraph), "paragraph")



    def test_markdown_to_html_node(self):
        markdown = """
# This is a heading



This is a paragraph of text."""

        html_nodes = markdown_to_html_node(markdown).to_html()
        self.assertEqual(
            html_nodes,
            "<div><h1>This is a heading</h1><p>This is a paragraph of text.</p></div>"
           )

        markdown = """
- list *italic*
- list `code`"""

        html_nodes = markdown_to_html_node(markdown).to_html()
        self.assertEqual(
            html_nodes,
            "<div><ul><li>- list <i>italic</i></li><li>- list <code>code</code></li></ul></div>"
           )
        

        markdown = """
1. **law**
2. and order"""
        html_nodes = markdown_to_html_node(markdown).to_html()
        self.assertEqual(
            html_nodes,
            "<div><ol><li>1. <b>law</b></li><li>2. and order</li></ol></div>"
           )
     


if __name__ == "__main__":
    unittest.main() 