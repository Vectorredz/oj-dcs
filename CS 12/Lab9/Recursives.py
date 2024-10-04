from typing import TypeVar, Sequence
T = TypeVar("T")

# List Membership

def is_member(elem: T, elems: Sequence[T]) -> bool:
    return (False if not elems else 
            True if elem == elems[0] else is_member(elem, elems[1:]))

# def test_cases():
#     assert is_member(0, []) == False
#     assert is_member(0, [0]) == True
#     assert is_member(0, [1, 2]) == False
#     assert is_member('c', ['a', 'b', 'c']) == True
# test_cases()

# Squaring A List Of Numbers

def square_nums(elems: Sequence[int]) -> list[int]:
    if not elems:
        return []
    else:
        return [elems[0] ** 2] + square_nums(elems[1:])
    
# def test_cases():
#     assert square_nums([]) == []
#     assert square_nums([1]) == [1]
#     assert square_nums([1, 2]) == [1, 4]
#     assert square_nums([1, 2, 3]) == [1, 4, 9]
# test_cases()

# Reversing

def reverse(elems: Sequence[int]) -> list[int]:
    if not elems:
        return []
    else:
        return [elems[-1]] + reverse(elems[:-1])

# def test_cases():
#     assert reverse([]) == []
#     assert reverse([1]) == [1]
#     assert reverse([1, 2]) == [2, 1]
#     assert reverse([1, 2, 3]) == [3, 2, 1]
# test_cases()

# Removing Odd Numbers

def without_odds(elems: Sequence[int]) -> list[int]:
    return ([] if not elems else [elems[0]] + without_odds(elems[1:]) 
            if elems[0] % 2 == 0 else without_odds(elems[1:]))

# def test_cases():
#     assert without_odds([]) == []
#     assert without_odds([1]) == []
#     assert without_odds([2]) == [2]
#     assert without_odds([1, 2]) == [2]
#     assert without_odds([2, 1]) == [2]
#     assert without_odds([1, 3, 5]) == []
#     assert without_odds([1, 2, 3, 4, 5]) == [2, 4]
# test_cases()

# Generating All Subsets:

def powerset(elems: Sequence[T]) -> list[list[T]]:
    if not elems:
        return [[]]
    else:
        return powerset(elems[1:]) + [[elems[0]] + subset for subset in powerset(elems[1:])]

# Insert
def insert(elem: int, sorted_elems: Sequence[int]) -> list[int]:
    return ([elem] if not sorted_elems else [elem] + list(sorted_elems) 
                if elem < sorted_elems[0] else [sorted_elems[0]] + insert(elem, sorted_elems[1:]))

# def test_cases():
#     assert insert(1, []) == [1]
#     assert insert(5, [10, 20, 30]) == [5, 10, 20, 30]
#     assert insert(15, [10, 20, 30]) == [10, 15, 20, 30]
#     assert insert(25, [10, 20, 30]) == [10, 20, 25, 30]
#     assert insert(35, [10, 20, 30]) == [10, 20, 30, 35]
# test_cases()

# Insertion Sort

def insertion_sort(elems: Sequence[int]) -> list[int]:
    return [] if not elems else insert(elems[0], insertion_sort(elems[1:]))
    
# def test_cases():
#     assert insertion_sort([]) == []
#     assert insertion_sort([1]) == [1]
#     assert insertion_sort([20, 10]) == [10, 20]
#     assert insertion_sort([10, 20, 30]) == [10, 20, 30]
#     assert insertion_sort([30, 10, 20]) == [10, 20, 30]
#     assert insertion_sort([30, 20, 10]) == [10, 20, 30]
# test_cases()

# Recursive Max

def my_max(elems: Sequence[int]) -> int:
    return (0 if not elems else elems[0] 
            if elems[0] > my_max(elems[1:]) else my_max(elems[1:]))

# def test_cases():
#     assert my_max([1]) == 1
#     assert  my_max([20, 10]) == 20
#     assert  my_max([10, 20, 30]) == 30
#     assert  my_max([30, 10, 20]) == 30
#     assert my_max([30, 20, 10]) == 30
# test_cases()

# Recursive Selection Sort

def selection_sort(elems: Sequence[int]) -> list[int]:
    return ([] if not elems else ([elems[0]] + selection_sort(elems[1:])
            if elems[0] < my_max(elems) else selection_sort(elems[1:]) + [my_max(elems)]))

# def test_cases():
#     assert selection_sort([]) == []
#     assert selection_sort([1]) == [1]
#     assert selection_sort([20, 10]) == [10, 20]
#     assert selection_sort([10, 20, 30]) == [10, 20, 30]
#     assert selection_sort([30, 10, 20]) == [10, 20, 30]
#     assert selection_sort([30, 20, 10]) == [10, 20, 30]
# test_cases()

def is_palindrome(s: str) -> bool:
    return (True if s == '' 
            else ( is_palindrome(s[1:-1]) if s[0] == s[-1] 
            else False))
print(is_palindrome("ttarratt"))

def pow(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)
    
print(pow(2, 5))

def fib(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

    
print(fib(4))

arr= [[1,2], [1,2]]
print(*arr)