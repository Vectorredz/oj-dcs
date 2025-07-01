# Function to add an edge between two vertices
def addEdge(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

def displayAdjList(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{{{j[0]}, {j[1]}}} ", end="")
        print()

def main():
  
    # Create a graph with 3 vertices and 3 edges
    V = 3
    adj = [[] for _ in range(V)]

    # Now add edges one by one
    addEdge(adj, 1, 0, 4)
    addEdge(adj, 1, 2, 3)
    addEdge(adj, 2, 0, 1)

    print("Adjacency List Representation:")
    displayAdjList(adj)

if __name__ == "__main__":
    main()