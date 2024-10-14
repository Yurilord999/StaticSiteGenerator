from textnode import *
from htmlnode import *

def main():
    Textnode = TextNode("hello","bold","https://yea")
    print(Textnode)
    HtmlNode = HTMLNode("a", "text", ["tags", "tag"], {"href": "https://www.google.com","target": "blank"})
    print(HtmlNode)
    print(HtmlNode.props_to_html())

main()
