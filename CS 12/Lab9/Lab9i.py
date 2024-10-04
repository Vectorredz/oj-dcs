from typing import Sequence

def min_boxes(sheets: Sequence[int], k: int) -> int:
    return len(min_solver(insertion_sort(sheets), k, []))

def insertion_sort(sheets: Sequence[int]) -> list[int]:
    return [] if not sheets else insert(sheets[0], insertion_sort(sheets[1:]))

def insert(elem: int, sheets: Sequence[int]) -> list[int]:
    return [elem] if not sheets else [elem] + list(sheets[:]) if elem < sheets[0] else [sheets[0]] + insert(elem, sheets[1:]) 

def min_solver(sorted_elems: list[int], k: int,  curr: list[int]) -> list[list[int]]:
    return [] if not sorted_elems else ([curr + [sorted_elems[0], sorted_elems[-1]]] + min_solver(sorted_elems[1:-1], k, []) if (sorted_elems[0] + sorted_elems[-1]) <=  k 
                else [curr + [sorted_elems[-1]]] + min_solver(sorted_elems[:-1], k, []))

    

print(min_boxes((5,7,2,3), 8))