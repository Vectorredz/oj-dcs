from dataclasses import dataclass
@dataclass
class Node:
    val: int
    l: "Node | None" = None
    r: "Node | None" = None
    
def _in_order(root: Node | None) -> Node | None:
    if root is None:
        return root
    else:
        _in_order(root.l)
        print(root.val)
        _in_order(root.r)
        return 
    
# BST contains

def _contains(node, val):
    if (node is None):
        return False
    elif (node.val < val):
        return _contains(node.r, val)
    elif (node.val > val):
        return _contains(node.l, val)
    elif (node.val == val):
        return True

    
# BST add

def _add(node: Node | None, value: int) -> Node | None:
    # assert contains(node, value)
    if node is None:
        return Node(value, None, None)
    elif node.val == value:
        return None
    elif node.val > value:
        node.l = _add(node.l, value)
        return node
    elif node.val < value:
        node.r = _add(node.r, value)
        return node
    
# BST remove

def remove_leftmost(node):
    # assert node is not None
    if node.l is None:
        return node.val, node.r
    else:
        v, x = remove_leftmost(node.l)
        node.l = x
        return v, node

def remove(node, val):
    assert _contains(node, val)
    if val == node.val:
        if node.r is not None:
            # take the smallest value from the right tree
            (value, subtree) = remove_leftmost(node.r)
            node.r = subtree
            node.val = value
            return node
        else:
            return node.l
    if val < node.val:
        node.l = remove(node.l, val)
        return node
    if val > node.val:
        node.r = remove(node.r, val)
        return node

# BST next_larger 
def next_larger(node, val):
    if node is None: return None
    
    if val < node.val:
        ret = next_larger(node.l, val)
        if ret is not None:
            return ret
        return node.val
    else:
        return next_larger(node.r, val)

# BST next_smaller
def next_smaller(node, val):
    if node is None: return None
    
    if val > node.val:
        res = next_smaller(node.r, val)
        if res is not None:
            return res
        return node
    else:
        return next_smaller(node.l, val)


class OrderedSet:
    def __init__(self):
        self.root = None
        super().__init__()

    def add(self, val):
        self.root = _add(self.root, val)
        
    def remove(self, val):
        self.root = remove(self.root, val)

    def contains(self, val):
        return _contains(self.root, val)

    def next_larger(self, val):
        return next_larger(self.root, val)
    
    def in_order(self):
        return _in_order(self.root)
    
order = OrderedSet()
order.in_order()
