

def best_rolls(softness_vals: list[int], k: int) -> list[int]:
    variance: list[int] = []
    arr_sorted = sorted(softness_vals)
    minimum: int = 100
    hash_table: dict[int, list[int]] = {}
    for i in range(len(arr_sorted)):
        if (len(arr_sorted[i:k+i]) == k):
            variance: int = abs(max(arr_sorted[i:k+i]) - min(arr_sorted[i:k+i]))
            if (minimum >= variance):
                minimum = variance
                if (minimum not in hash_table):
                    hash_table[minimum] = arr_sorted[i:k+i]
    
    ret: list[int] = list(map(lambda x: softness_vals.index(x), hash_table[minimum]))
    return ret

print(best_rolls([123, 456, 789, 12, 345, 678, 901], 2)
)