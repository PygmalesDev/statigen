import unittest

from src.nodes.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init_plain(self):
        self.assertFalse("<" in LeafNode(value="This is a test leaf node").to_html())
    
    def test_with_props(self):
        self.assertTrue('<g tag="normal" ordinals="contained">' in LeafNode(tag="g", value="TestValue", props={"tag": "normal", "ordinals": "contained"}).to_html())


if __name__ == '__main__':
    unittest.main()
