def make_grid_graph(graph):
    i = 0
    edges = []
    rows = len(graph)
    cols = len(graph[0])
    mat = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] != '!':
                mat[r][c] = i
                i += 1
            else:
                mat[r][c] = "!"
    for r in range(rows):
        for c in range(cols):
            if (rows == 1):
                if (0 <= c < cols - 1 and r == 0):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
            elif (cols == 1):
                if (0 <= r < rows -1 ):
                    if (mat[r+1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r+1][c]))
            else:
                if (c == 0 and r == 0):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                if (0 < c < cols-1 and r == 0):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                if (c == 0 and 0 < r < rows-1):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
                if (0 < c < cols-1 and 0 < r < rows-1):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
                if (c == cols-1 and 0 < r < rows-1):
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
                if (c == 0 and r == rows-1):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
                if (0 < c < cols-1 and r == rows-1):
                    if (mat[r][c+1] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r][c+1]))
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
                if (c == cols-1 and r == rows-1):
                    if (mat[r-1][c] != "!" and (mat[r][c] != "!")):
                        edges.append((mat[r][c], mat[r-1][c]))
    return (i, edges)



    # for r in range(len(matrix)):
    #     for c in range(len(matrix[0])):
    #         print(matrix[r][c], end=" ")  
    #     print("") 


graph = (' ',
         ' ', 
         ' ')


print(make_grid_graph((graph)))
