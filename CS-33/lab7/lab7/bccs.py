# Idea here
# 1. Check first if its simple graph
# 2. Create adj list
# 3. Visit
# 4. Extract bccs

"""
Pseudo-code

def bridges_articulaation_points and bccs (n,edges):
    1. Initialize the stuffs and check for simple
    check if there is a self loops
    adj_list <- create_adj_list()
    # initialize disc, low, time
    
    2. Helper visit
    def visit(i):
        nonlocal time 
        update disc[i] <- time
        time += 1
    
    # initialize bridges, ap_points, edge_visited, edge_stack, bccs
   
    3. Extract bccs edge among the edge_stack
    def extract_bccs(edge):
        pop until edge is popped
        while True:
            last_edge <- edge_stack.pop()
            yield last_edge
            if last_edge is passed edge <- return
            
    4. Perform traversal
    def dfs(i, parent_edge):
        visit(i)
        is_root = parent_edge is None
        low[i] <- disc[i] // initialize the low and disc 
        found_isolated_child = False
        children = 0
        
        for idx, edge from adj[i]:
            if edge_idx is in edge_visited: continue
            edge_visied[edge_idx] <- True
            
            if disc[j] == -1:
            
    
    
    
"""