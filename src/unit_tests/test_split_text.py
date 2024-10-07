import unittest

from src.utils.functools import split_markdown
from src.utils.constants import TextType
from src.nodes.textnode import TextNode

class TestSplitText(unittest.TestCase):
    def test_split_raw(self):
        result = split_markdown("Hello, world!")
        print(result.to_html())

    def test_split_typed(self):
        result = split_markdown("This text contains **bold**, *italic* and `code` formatting types, as well as plain text")
        print(result.to_html())
    
    def test_split_multiple_paragraphs(self):
        result = split_markdown(
        """This text is split in multiple lines. **This is the first paragraph and its bold**. But not entirely!!\n\nThis is the second paragraph, and its written in *italic*. How cool is that!\n\nThis is the third line and it contains some `code lines`. Awesome""")
        print(result.to_html())
    
    def test_nested_formatting(self):
        result = split_markdown("This text contains **some nasty *nested* formatting `thingies`. I really hate them *but there's no other way*. Ehe**")
        print(result.to_html())
    
    def test_formatted_paragraps(self):
        result = split_markdown("""**Here are some formatted paragraphs**\n\n*Sometimes there's only one way to make it right*\n\n*I've chosen this **path** myself...*""")
        print(result.to_html())

    def test_format_empty(self):
        result = split_markdown("")
        print(result.to_html())
    
    def test_extract_links(self):
        result = split_markdown("This text **contains** ![image](https://imgs.org) - an image, and a link to a website: [link to a website](https://website.org)! So awesome")
        print(result.to_html())

if __name__ == '__main__':
    unittest.main()
