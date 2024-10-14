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

    def test_text_node_to_html_node(self):
        node = TextNode("text", "text", "url")
        node2 = TextNode("text", "bold", "url")
        node3 = TextNode("text", "italic", "url")
        node4 = TextNode("text", "code", "url")
        node5 = TextNode("text", "link", "url")
        node6 = TextNode("text", "image", "url")
        node7 = TextNode("text", "None", "url")
        html = text_node_to_html_node(node)
        html2 = text_node_to_html_node(node2)
        html3 = text_node_to_html_node(node3)
        html4 = text_node_to_html_node(node4)
        html5 = text_node_to_html_node(node5)
        html6 = text_node_to_html_node(node6)
        self.assertEqual(html.tag, None)
        self.assertEqual(html2.tag, "b")
        self.assertEqual(html3.tag, "i")
        self.assertEqual(html4.tag, "code")
        self.assertEqual(html5.tag, "a")
        self.assertEqual(html5.props, {"href": "url"})
        self.assertEqual(html6.tag, "img")
        self.assertEqual(html6.value, "")
        self.assertEqual(html6.props, {"src": "url", "alt": "text"})
        
        with self.assertRaises(Exception):
            text_node_to_html_node(node7)


if __name__ == "__main__":
    unittest.main()
    