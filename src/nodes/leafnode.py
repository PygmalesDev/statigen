from src.nodes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=dict()):
        super().__init__(tag, value, None, props)

    def to_html(self, recursion=0):
        if self.value == None:
            raise ValueError("No value was set for the LeafNode!")
        return ('\n'+'\t'*recursion+f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" if self.tag != None else '\n'+'\t'*recursion+self.value) 
        
