from typing import Sequence

def generating_subsets(d: Sequence[int], i: int, curr: list[int]) -> list[list[int]]:
    return [curr] if i == len(d) else generating_subsets(d, i + 1, curr + [d[i]]) + generating_subsets(d, i + 1, curr)

def sum_of_subsets(subsets: list[list[int]], i: int, j: int, curr_sum: int) -> list[int]:
    return [curr_sum] if i == len(subsets) else [curr_sum] + sum_of_subsets(subsets, i+1, 0, 0) if j == len(subsets[i]) else sum_of_subsets(subsets, i, j+1, curr_sum + subsets[i][j])
def filter_subsets(sums: list[int], x: int, y: int) -> int:
    return 0 if not sums else (1 + filter_subsets(sums[1:], x, y) if y >= sums[0] >= x else filter_subsets(sums[1:], x , y))

def num_problem_sets(d: Sequence[int], x: int, y: int) -> int:
    return filter_subsets(sum_of_subsets(generating_subsets(d, 0, []), 0, 0, 0), x, y)

print(num_problem_sets((4, 2, 5, 2, 6), 6, 10))