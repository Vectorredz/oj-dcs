from dataclasses import dataclass, field

@dataclass 
class Node:
    label: int
    val: int 
    adj: "list[Node]" = field(default_factory=list)
    parent: "Node | None" = None
    top_child: "Node | None" = None
    min_to_root: int = 0
    size: int = 0
    
    def traverse(self):
        self.parent = self
        self._traverse()
    
    def _traverse(self):
        self.size = 1
        for child in self.adj:
            if child is not self.parent:
                child.parent = self
                self._traverse()
                self.size += child.size
                
    def compute_stuff(self):
        self.top_child = self if (self is self.parent) or (self.parent.parent is self.parent) else self.parent.top_child
        self.min_to_root = self.val
        if self.parent is not self:
            self.min_to_root = min(self.min_to_root, self.parent.min_to_root)
        
        for child in self.adj:
            if child is not self.parent:
                child.compute_stuff()
                
    def find_centroid(self):
        self.traverse()
        n = self.size
        while True:
            for node in self.adj:
                if node is not self.parent and node.size * 2 > n:
                    self = node
                    break
            else:
                break
        return self
    
    def solve_path_mins(self, queries):
        self = self.find_centroid()
        
        self.traverse()
        self.compute_stuff()
        
        child_queries = {node.label: {} for node in self.adj}
        for query in queries:
            if query.i.top_child is query.j.top_child and query.j.top_child is not self:
                child_queries[query.i.top_child.label].append(query)
            else:
                assert query.ans is None
                query.ans = min(query.i.min_to_root, query.j.min_to_root)

        