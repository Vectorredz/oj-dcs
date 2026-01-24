from collections import defaultdict
def best_rolls(softness_vals: list[int], k: int) -> list[int]:
    sorted_vals = sorted(softness_vals)
    index_map = defaultdict(list)
    minimum = float('inf')
    start = 0
    end = 0 
    for idx, val in enumerate(softness_vals):
        index_map[val].append(idx)
    # sliding window proper
    # no slice 
    for i in range(len(sorted_vals)):
        if (i < len(sorted_vals)-k+1):
            variance = abs(sorted_vals[i] - sorted_vals[k+i-1])
            if (variance < minimum):
                minimum = variance
                start = i
                end = k+i
    best = sorted_vals[start:end]
    ret = []
    # find the indices 
    for idx in best:
        ret.append(index_map[idx].pop())
        
    return sorted(ret)
# assert best_rolls([5], 1) == [0]  # Expected: [0]
# assert best_rolls([5, 2, 8, 3], 4) == [0,1,2,3]
# assert best_rolls([7,7,7,7], 2) == [0,1]
# best_rolls([1,2,3], 5)