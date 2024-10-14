import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        node = HTMLNode("a","a",None,{"href": "url", "target": "_blank"})
        self.assertEqual(node.props_to_html(),
                         ' href="url" target="_blank"'
                         )
    
    def test_not_eq_props(self):
        node = HTMLNode("a","a",None,{"href": "url2", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(),
                         'href="url" target="_blank"'
                         )

    def test_repr(self):
        node = HTMLNode("a", "text", ["tag"], {"href": "url"})
        self.assertEqual(repr(node),
                         "HTMLNode(a, text, ['tag'], {'href': 'url'})")

    def test_to_html(self):
        node = HTMLNode("a", "text", ["tag"], {"href": "url"})
        with self.assertRaises(NotImplementedError): 
            node.to_html()

if __name__ == "__main__":
    unittest.main()
    