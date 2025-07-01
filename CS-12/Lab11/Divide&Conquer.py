from __future__ import annotations
from typing import Generic, TypeVar, Callable
from dataclasses import dataclass
 
T = TypeVar('T')
 
@dataclass
class TreeNode(Generic[T]):
    value: T
    children: list[TreeNode[T]]

# Tree Sum
def tree_sum(root: TreeNode[int]) -> int:
    return root.value + sum([tree_sum(child) for child in root.children])

# Tree Height
def tree_height(root: TreeNode[int]) -> list[int]:
    return [len(tree_height(child)) for child in root.children]

# Tree Count
def count(root: TreeNode[T]) -> int:
    return 1 if not root.children else 1 + len([count(child) for child in root.children])

# Tree Max
def tree_max(root: TreeNode[int]):
    ret = root.value
    for child in root.children:
        currRet = child.value
        ret = max(ret, currRet)
    return ret

# Tree Count If
def count_if(pred: Callable[[T], bool], root: TreeNode[T]) -> int:
    count: int = 0
    ret = root.value
    if pred(ret):
        count += 1
    for child in root.children:
        count += count_if(pred, child)
    return count

def is_odd(val: int) -> bool:
    return True if val % 2 == 0 else False

from typing import TypeVar, Callable
 
# Assume TreeNode is defined
 
A = TypeVar('A')
B = TypeVar('B')


print(count_if(is_odd, TreeNode(10, [TreeNode(20, []), TreeNode(30, [])])))

Tree = TreeNode(
    value=10,
    children=[
        TreeNode(
            value=20,
            children=[
                TreeNode(
                    value=50,
                    children=[
                        TreeNode(value=80, children=[]),
                    ],
                ),
            ],
        ),
        TreeNode(value=30, children=[]),
        TreeNode(
            value=40,
            children=[
              TreeNode(value=60, children=[]),
              TreeNode(value=70, children=[]),
            ],
        ),
    ],
)

def test_cases():
    assert count(TreeNode(10, [])) == 1
    assert count(TreeNode(10, [TreeNode(20, [])])) == 2
    assert count(TreeNode(10, [TreeNode(20, []), TreeNode(30, [])])) == 3

    assert tree_max(TreeNode(10, [])) == 10
    assert tree_max(TreeNode(10, [TreeNode(20, [])])) == 20
    assert tree_max(TreeNode(20, [TreeNode(10, [])])) == 20
    
test_cases()