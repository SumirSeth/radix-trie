from __future__ import annotations

"""
radix trie


              [r]
             /   \
         [oman]  [ub]
        /     \     \
     [e]    [us]   [ens]
                      \
                    [er]
              
"""
class Node():
    """
    Node: Represents a Node of a RadixTree
    """
    def __init__(self, label:str = "", children:dict[str, Node] | None = None, is_word:bool = False):
        self.label = label
        self.children = children if children is not None else {}
        self.is_word = is_word

    def is_leaf(self):
        return True if self.children == {} else False




n = Node("Test")
s = Node("S Node", n)
print(s.is_leaf())
