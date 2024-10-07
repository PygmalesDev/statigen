from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode

def split_markdown(text: str) -> ParentNode:
    parents = list(map(lambda parag: tokenize_paragraph(parag), text.split("\n\n")))
    return ParentNode(children=parents) if len(parents) > 1 else parents[0]

def tokenize_paragraph(parag: str, parentag: str = 'p') -> ParentNode:
    nodes = []

    st_ind = 0 
    indxl = 0

    def move_index(mov: int):
        nonlocal st_ind, indxl

        indxl = mov
        st_ind = indxl+1

    def substr(start: int = None, end: int = None):
        nonlocal parag

        return (parag[start:] if end is None 
                else parag[:end] if start is None 
                else parag[start:end])

    def lit(index: int = 0) -> str:
        nonlocal parag

        return parag[index]
    
    # Iterate the text body from the first letter to the last. 
    # Split text parts on raw and formatted upon finding key symbols.
    while indxl < len(parag)-1:
        lit = parag[indxl]

        match lit:
            case '!' | '[':     
                link_node, indxn = extract_link(substr(indxl))
                if link_node is not None:
                    nodes.append(get_raw_leaf(parag, st_ind, indxl))
                    nodes.append(link_node)
                    move_index(indxl+indxn)

            case '*' | '`':
                if False:
                    pass
                else:
                    indxtxt = 1 if parag[indxl+1] == lit else 0 
                    indxn = indxl + indxtxt + substr(indxl+indxtxt+1).find(lit+lit*indxtxt) + 1
                    
                    txtag = 'code'
                    if lit == '*':
                        if indxtxt > 0: txtag = 'b'
                        else: txtag = 'i'
                        
                    nodes.append(get_raw_leaf(parag, st_ind, indxl))

                    body = substr(indxl+indxtxt+1, indxn)
                    if '*' in body or '`' in body: nodes.append(tokenize_paragraph(body, txtag))
                    else: nodes.append(LeafNode(value=body, tag=txtag))

                    move_index(indxn+indxtxt)
            
        indxl +=1

    if st_ind != indxl: nodes.append(get_raw_leaf(parag, st_ind))
    
    return ParentNode(tag=parentag, children=nodes)


def extract_link(text: str) -> (str, int):
    if all((let in text for let in ['[', ']', '(', ')'])):
        end = text.index(')')

        val = text[text.index('[')+1:text.index(']')]
        url = text[text.index('(')+1:end]
        tg = 'img' if '!' in text[:end] else 'a'
        return LeafNode(tag=tg, value=val, props={"url": url}), end
    return None, None

def get_raw_leaf(body:str, st_indx: int, end_indx: int = 0) -> LeafNode:
        return (LeafNode(value=body[st_indx:end_indx]) if end_indx != 0 
                else LeafNode(value=body[st_indx:]))
