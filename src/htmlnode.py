class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              #String representing HTML tag 
        self.value = value          #String representing value of tag
        self.children = children    #list of HTMLNode objects representing children of this node
        self.props = props          #dict of k-v pairs representing attributes {"href": "url"}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        printed = ""
        for key in self.props:
            printed += f' {key}="{self.props[key]}"'
        return printed
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})' 