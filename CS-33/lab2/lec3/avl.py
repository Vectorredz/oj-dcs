from dataclasses import dataclass
@dataclass
class Node:
    val: int
    h: int = 0
    l: "Node | None" = None
    r: "Node | None" = None

    def reset_height(self):
        # height h of the tree
        self.h = max(height(self.l), height(self.r)) + 1

def join(l, x, r):
    # left subtree as the left split
    x.l = l
    # right subtree as the right split
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
        # unbalanced tree s.t. bf > 1 where heavy left-heavy
        if height(x.l) - height(x.r) >= 2:
            # LR-rotation
            if height(x.l.l) < height(x.l.r):
                x.l = left_rotate(x.l)
            # RR rotation
            x = right_rotate(x)
        elif height(x.r) - height(x.l) >= 2:
            # RL-rotation
            if height(x.r.r) < height(x.r.l):
                x.r = right_rotate(x.r)
            # LL-ROTATION
            x = left_rotate(x)
    return x

def add(node, val):
    return rebalance(_add(node, val))

def _add(node, val):
    if (node is None):
        return Node(val, 0, None, None)
    elif (val > node.val):
        node.r = _add(node.r, val)
    elif (val < node.val):
        node.l = _add(node.l, val)
    else:
        assert val == node.val
    return node

def contains(node, val):
    if (node is None):
        return False
    elif (val < node.val):
        return contains(node.l, val)
    elif (val > node.val):
        return contains(node.r, val)
    elif (val == node.val):
        return True
    
def remove_leftmost(node):
    assert node is not None

    if node.l is None:
        return node.val, node.r
    else:
        v, x = remove_leftmost(node.l)
        node.l = x
        return v, node

def remove(node, val):
    return rebalance(_remove(node, val))

def _remove(node, val):
    if (node is None):
        return None
    elif (val > node.val):
        node.r = _remove(node.r, val)
        return node
    elif (val < node.val):
        node.l = _remove(node.l, val)
        return node
    elif (val == node.val):
        if node.r is None:
            return node.l
        else:
            v,x = remove_leftmost(node.r)
            node.r = x
            node.val = v
            return node
            