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
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
  
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML. No tag provided for ParentNode")
        if self.children == None:
            raise ValueError("Invalid HTML. No children provided for ParentNode")
        html_children = ""
        for child in self.children:
            html_children += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>'


    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
