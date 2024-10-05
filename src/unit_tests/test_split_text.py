import unittest

from src.utils.functools import split_markdown_text
from src.utils.constants import TextType
from src.nodes.textnode import TextNode

class TestSplitText(unittest.TestCase):
    def test_split_raw(self):
        result = split_markdown_text("Hello, world!")
        self.assertEqual(1, len(result))
        self.assertEqual(result[0], TextNode("Hello, world!", TextType.TEXT))

    def test_split_typed(self):
        result = split_markdown_text("This text contains **bold**, *italic* and `code` formatting types, as well as plain text")


if __name__ == '__main__':
    unittest.main()
