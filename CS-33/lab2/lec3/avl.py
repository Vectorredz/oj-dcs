
# join
# height
# left_rotate
# right_rotate
# rebalance
# add
# contains
# remove
# remove_leftmost

from dataclasses import dataclass

@dataclass
class Node:
    val: int
    h: int = 0
    l: "Node | None" = None
    r: "Node | None" = None
    
    def reset_height(self):
        self.h = max(height(self.l), height(self.r)) + 1
    
def contains(node, val):
    if (node is None):
        return None
    elif (val > node.val):
        return contains(node.r, val)
    elif (val < node.val):
        return contains(node.l, val)
    
def join(l, x, r):
    x.l = l
    x.r = r
    x.reset_height()
    return x

def height(node):
    return -1 if node is None else node.h

def left_rotate(x):
    (a, b, c, d, e) = (x.l, x, x.r.l, x.r, x.r.r)
    return join(join(a, b, c), d, e)

def right_rotate(x):
    (a, b, c, d, e) = (x.l.l, x.l, x.l.r, x, x.r)
    return join(a, b, join(c, d, e))

def rebalance(x):
    if x is not None:
        x.reset_height()
        # ll rotation
        if (height(x.l) >= height(x.r) + 2):
            if (height(x.l.l) < height(x.r.l)):
                x.l = left_rotate(x)
            x = right_rotate(x)
        elif (height(x.r) >= height(x.l) + 2):
            if (height(x.r.r) < height(x.r.l)):
                x.r = right_rotate(x)
            x = left_rotate(x)
    return x

def _add(node, val):
    if (node is None):
       return Node(val, 0, None, None) 
    elif val > node.val:
        node.r = _add(node.r, val)
        return node
    elif val < node.val:
        node.l = _add(node.l, val)
        return node
    elif val == node.val:
        return None

def add(node, val):
    return rebalance(_add(node, val))

def _remove_leftmost(node):
    if node.l is None: 
        return node.val, node.r
    (val, subtree) = _remove_leftmost(node.l)
    node.l = subtree
    node.val = val
    return val, node

def remove_leftmost(node):
    val, node = _remove_leftmost(node)    
    return val, rebalance(node)


