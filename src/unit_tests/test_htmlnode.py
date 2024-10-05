import unittest

from src.nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_creation(self):
        self.assertEqual(str(HTMLNode()), "HTMLNode(None, None, None, {})")
        self.assertEqual(str(HTMLNode(value="tag")), "HTMLNode(None, tag, None, {})")

    def test_props_to_html(self):
        node = HTMLNode(props={"color": "blue", "stage": "second"})
        self.assertEqual(node.props_to_html(), ' color="blue" stage="second"')

        node =  HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
