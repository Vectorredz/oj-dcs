from dataclasses import dataclass
from collections.abc import Sequence
@dataclass
class Node:
    num: int
    level: int
    l: "Node | None" = None
    r: "Node | None" = None
    h: int = 0

    def reset_height(self):
        self.h = max(height(self.l), height(self.r)) + 1

def height(node):
    return -1 if node is None else node.h

def join(l, x, r):
    x.l = l
    x.r = r
    x.reset_height()
    return x
   
def left_rotate(x):
    (a, b, c, d, e) = (x.l, x, x.r.l, x.r, x.r.r)
    return join(join(a, b, c), d, e)

def right_rotate(x):
    (a, b, c, d, e) = (x.l.l, x.l, x.l.r, x, x.r)
    return join(a, b, join(c, d, e))

def rebalance(x):
    if x is not None:
        x.reset_height()
        if height(x.l) >= height(x.r) + 2:
            if height(x.l.l) < height(x.l.r):
                x.l = left_rotate(x.l)
            x = right_rotate(x)
        elif height(x.r) >= height(x.l) + 2:
            if height(x.r.r) < height(x.r.l):
                x.r = right_rotate(x.r)
            x = left_rotate(x)
    return x

def _insert(node, val, level):
    if node is None:
        return Node(val, level, None, None, 0)

    if val < node.num:
        node.l = _insert(node.l, val, level)
    elif val > node.num:
        node.r = _insert(node.r, val, level)
    else:
        return node  # duplicate, ignore

    return rebalance(node)   # rebalance as you return


def insert(node, val, level):
    return rebalance(_insert(node, val, level))
    
def _sum(node, min, max):
    if node is None:
        return 0
    else:
        if min <= node.num <= max:
            left = _sum(node.l, min, max)
            right = _sum(node.r, min, max)
            return node.level + left + right
        else:
            if node.num > min:
                return _sum(node.l, min, max)
            elif node.num < max:
                return _sum(node.r, min, max)
        # if node.num < min:
        #     return _sum(node.r, min, max)
        # elif node.num > max:
        #     return _sum(node.l, min, max)
        # else:
        #     return node.level + _sum(node.l, min, max) + _sum(node.r, min, max)

def remove_leftmost(node):
    if node.l is None:
        return node.num, node.level, node.r
    else:
        (val, lvl,  sub_tree) = remove_leftmost(node.l)
        node.l = sub_tree
        return val, lvl, node

        
def _remove(node, val):
    if node is None: 
        return None
    if node.num > val:
        node.l = _remove(node.l, val)
    elif node.num < val:
        node.r = _remove(node.r, val)
    else:
        if node.r is None:
            return node.l
        else:
            val_succ, lvl_succ, subtree = remove_leftmost(node.r)
            node.num = val_succ
            node.level = lvl_succ
            node.r = subtree
    return rebalance(node)  # rebalance every ancestor



class PokemonTeam:
    def __init__(self, initial_team: Sequence[tuple[int, int]]):
        self.teams = initial_team
        
        self.root = None
        
        for mem in self.teams:
            v, l = mem
            self.root = insert(self.root, v, l)
        
    def add(self, i: int, l: int):
        self.root = insert(self.root, i, l)
        
    def remove(self, i: int):
        self.root = rebalance(_remove(self.root, i))

    def sum(self, i: int, j: int) -> int:
        return _sum(self.root, i, j)
        
# team = PokemonTeam([(6, 100), (1, 2), (5, 1)])
# assert team.sum(1, 5) == 3
# team.add(3, 5)
# assert team.sum(1, 5) == 8
# team.remove(1)
# assert team.sum(1, 5) == 6
# team.remove(1)
# assert team.sum(1, 5) == 6
# assert team.sum(7, 11) == 0

