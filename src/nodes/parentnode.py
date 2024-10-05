from src.nodes.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag="p", props=dict()):
        super().__init__(tag, None, children, props)

    def to_html(self, recursion=0):
        if self.children == None or (self.children) == 0:
            raise ValueError("ParentNode doesn't contain children values")
        return '\n' + '\t'*recursion + f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(recursion+1), self.children))}'+'\n'+'\t'*recursion+f'</{self.tag}>'
