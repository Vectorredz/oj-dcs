# pyright: strict

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    children: Sequence[Node] = ()


# def max_path(node: Node) -> list[list[int] | int]:
#     ret = node.value
#     total_files: list[list[int] | int] = []
#     def node_collector(n: Node):
#         root = n.value
#         curr_files: list[int] = []
#         for child in n.children:
#             curr_files.append(node_collector(child))
#         if curr_files:
#             total_files.append(curr_files)
#         return root
    
#     node_collector(node)
#     total_files.append(ret)
#     return total_files

def max_path(node: Node) -> int:
    ret: int = node.value
    def node_collector(n: Node) -> int:
        nonlocal ret
        root = n.value
        if not root:
            return 0
        children_val: list[int] = []
        for child in n.children:
            children_val.append(node_collector(child))
        
        children_val.sort(reverse=True)
        first_max = children_val[0] if len(children_val) > 0 else 0
        second_max = children_val[1] if len(children_val) > 1 else 0

        ret = max(ret, root + first_max + second_max)
        return root + max(first_max, second_max)
    node_collector(node)
    return ret
         

print(max_path(Node(value=1, children=
                    [Node(value=2, children=
                          [Node(value=4, children=[]), 
                           Node(value=5, children=
                                [Node(value=6, children=[])])]), 
                    Node(value=3, children=[])])))

