import unittest

from src.nodes.textnode import TextNode
from src.utils.constants import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_nourl(self):
        node = TextNode("TestNode", TextType.ITALIC)
        self.assertEqual(node.url, None)

    def test_noneq(self):
        node = TextNode("Node1", TextType.ITALIC)
        node2 = TextNode("Node2", TextType.TEXT)
        self.assertFalse(node == node2)


if __name__ == "__main__":
    unittest.main()
