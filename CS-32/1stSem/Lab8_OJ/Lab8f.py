from collections import deque

def flea_sum(vert, edges, init_state):
    n = len(vert)
    adj_list = {i: [] for i in range(n)}
    for u, w in edges:
        adj_list[u].append(w)
        adj_list[w].append(u)

    queue = deque([init_state])
    visited = set([init_state])
    total_sum = 0

    while queue:
        state = queue.popleft()
        i1, i2, i3 = state
        
        state_value = vert[i1] * vert[i2] * vert[i3]
        total_sum += state_value

        for new_i1 in adj_list[i1]:
            for new_i2 in adj_list[i2]:
                for new_i3 in adj_list[i3]:
                    new_state = (new_i1, new_i2, new_i3)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)

    return total_sum

print(flea_sum((3, 1, 4), (
    (0, 2),
    (1, 1),
), (0, 1, 2)))