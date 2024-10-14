import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic", None)
        self.assertEqual(node, node2)

    def test_eq_types(self):
        node = TextNode(None, 10, "hello")
        node2 = TextNode(None, 10, "hello")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node,node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node,node2)
    
    def test_not_eq_types(self):
        node = TextNode("1", "bold")
        node2 = TextNode(1, "bold", None)
        self.assertNotEqual(node,node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "url")
        self.assertEqual("TextNode(This is a text node, bold, url)", repr(node))



if __name__ == "__main__":
    unittest.main()
    