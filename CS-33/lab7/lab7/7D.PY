from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class Edge:
    i: int 
    j: int 
    
def make_adj_list(n, edges):
        adj: list[list[int]] = [[] for _ in range(n + 1)]
        
        for idx, edge in enumerate(edges):
            i, j = edge.i, edge.j
            adj[i].append((j, idx, Edge(i,j)))
            adj[j].append((i, idx, Edge(j,i)))
        
        return adj        
            
def find_artic_pts(n, edges):
    
        adj =  make_adj_list(n,edges)

        # 1. self loops
        # assert any(e.i == e.j for e in edges)
        # 2. init vis, low
        vis = [-1] * n
        low = [-1] * n
        
        time = 0
        
        # 3. visit funciton
        def visit(i):
            nonlocal time 
            vis[i] = time
            time += 1        
    
        # 4. init bridges
        bridges = []
        ap = []
        edge_visited = [False] * len(edges)
        edge_stack = []
        bccs = []
        
        # 5. extract the bccs from edge_stack
        def extract_bccs(edge):
            # pop until edge is popped
            while True:
                last_edge = edge_stack.pop()
                yield last_edge
                if last_edge == edge: return
        
        # 6. do dfs  
        def dfs(i, parent_edge):
            # 7. init stuffs, setting 
            visit(i)
            is_root = parent_edge is None
            low[i] = vis[i]
            found_isolated_child = False
            children = 0
            
            for j, edge_idx, edge in adj[i]:
                
                if edge_visited[edge_idx]: continue
                
                edge_visited[edge_idx] = True

                if vis[j] == -1: # tree edge
                    edge_stack.append(edge)
                    dfs(j, edge)
                    low[i] = min(low[i], low[j])
                    
                    children += 1
                    
                    if low[j] > vis[i]: # bridges
                        bridges.append(edge)
                    
                    if low[j] >= vis[i]: # artic pts but the bcc!
                        bccs.append(list(extract_bccs(edge)))
                        found_isolated_child = True
                        
                elif edge is not parent_edge: # back edge
                    edge_stack.append(edge)
                    low[i] = min(low[i], vis[j]) # if there 2
                
            if not is_root and found_isolated_child or is_root and children >= 2:
                ap.append(i)
        
        if n > 0:
            dfs(1, None)

        # build block graph
        vertex_to_blocks = {v: [] for v in range(1, n+1)}
        block_graph = {}
        blocks = []

        for bcc_idx, bcc in enumerate(bccs):
            block_name = f"B{bcc_idx}"
            blocks.append(block_name)
            block_graph[block_name] = []
            block_vertices = set()
            for e in bcc:
                block_vertices.add(e.i)
                block_vertices.add(e.j)
            for v in block_vertices:
                vertex_to_blocks[v].append(block_name);
                block_graph.setdefault(v, []).append(block_name)
                block_graph[block_name].append(v)

        return {
            "articulation_points": ap,
            "bridges": bridges,
            "bccs": bccs,
            "block_graph": block_graph
        }

from pprint import pprint

pprint(find_artic_pts(6, (
    Edge(1,2),
    Edge(2,4),
    Edge(1,3),
    Edge(3,4),
    Edge(2,3),
    Edge(4,5),
    
)))