from src.utils.constants import TextType
from src.nodes.textnode import TextNode
from src.nodes.leafnode import LeafNode

def split_markdown_text(text: str) -> list[TextNode]:
    paragraphs = text.split('\n')
    nodes = []
    
    for parag in paragraphs:
        st_ind = 0 
        indxl = 0
        while indxl < len(parag)-1:
            lit = parag[indxl]

            if lit in ['*', '`']: 
                indxtxt = 1 if parag[indxl+1] == lit else 0 
                indxn = indxl + indxtxt + parag[indxl+indxtxt+1:].find(lit) + 1
                
                if indxn < indxl: raise Exception("Caught an error while tokenizing input string after index " + indxl)
                
                txtype = TextType.CODE
                if lit == '*':
                    if indxtxt > 0: txtype = TextType.BOLD
                    else: txtype = TextType.ITALIC

                nodes.append(TextNode(text=parag[st_ind:indxl], text_type=TextType.TEXT))
                nodes.append(TextNode(text=parag[indxl+indxtxt+1:indxn], text_type=txtype))

                indxl = indxn+indxtxt+1
                st_ind = indxl
            else:
                indxl +=1
            
        if st_ind != indxl:
            nodes.append(TextNode(text=parag[st_ind:], text_type=TextType.TEXT))

    return nodes

def textnode_to_htmlnode(node: TextNode) -> LeafNode:
    match node.text_type:
        case TextType.TEXT:
            return LeafNode(text=node.text)
        case TextType.BOLD:
            return LeafNode(text=node.text, tag="b")
        case TextType.ITALIC:
            return LeafNode(text=node.text, tag="i")
        case TextType.CODE:
            return LeafNode(text=node.text, tag="code")
        case TextType.LINK:
            return LeafNode(text=node.text, tag="a", props={"href":node.url})
        case TextType.IMAGE:
            return LeafNode(text="", tag="img", props={"src":node.url, "alt":node.text})
        case _:
            raise Exception("Tag parameter of the TextNode instance doesn't exist")
