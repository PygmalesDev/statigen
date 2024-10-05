import unittest

from src.nodes.parentnode import ParentNode
from src.nodes.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        self.assertTrue('<p>' in ParentNode(children=[LeafNode(tag="b", value="LeafNodeOne")]).to_html())

    def test_props(self):
        result = ParentNode(children=[LeafNode(tag="z", value="LeafNode", props={"prop": "val"})], props={"outer_prop": "outer_val"}).to_html()
        self.assertTrue('<p outer_prop="outer_val">' in result)
        self.assertTrue('<z prop="val">' in result)

    def test_deep_recursion(self):
        result = ParentNode(tag="a", children=[
            ParentNode(tag="b", children=[
                ParentNode(tag="c", children=[
                    LeafNode(tag="c_1l", value="Deep nested node of parent c"),
                    LeafNode(tag="c_2l", value="Second deep nested node of parent c", props={"prop_c_2l": "val"})
                    ], props={"prop_c": "another_val"}),
                LeafNode(tag="b_1l", value="Deep nested node of parent b", props={"prop_b_1l": "vall"}),
                LeafNode(tag="b_2l", value="Second deep nested node of parent b")
                ], props={"prop_b": "anv"})
            ]).to_html()

if __name__ == '__main__':
    unittest.main()
