import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):

    def test_eq_to_html(self):
        node = LeafNode("p", "text")
        node2 = LeafNode("a", "Click me!", {"href": "url"})
        self.assertEqual(node.to_html(),
                         '<p>text</p>'
                         )
        self.assertEqual(node2.to_html(),
                         '<a href="url">Click me!</a>'
                         )

    def test_no_value(self):
        node = LeafNode("a", None, {"href": "url"})
        with self.assertRaises(ValueError): 
            node.to_html()
    
    def test_no_tag(self):
        node = LeafNode(None, "text")
        self.assertEqual(node.to_html(),
                         'text'
                         )


if __name__ == "__main__":
    unittest.main()