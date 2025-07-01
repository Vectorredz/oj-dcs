from typing import Sequence, TypeVar

T = TypeVar("T")

def package_pila(p: Sequence[int], c: Sequence[T]) -> list[T]:
    return ([] if not p else 
            (list([c[0]]) + package_pila(list([p[0]-1]) + list(p[1:]), c) 
             if p[0] > 1 else [c[0]] + package_pila(p[1:], c[1:])))

print(package_pila((5,4), ('A', 'B')))

def test_package_pila():
    assert package_pila((3, 4), ('A', 'B')) == ['A', 'A', 'A', 'B', 'B', 'B', 'B'], f"{package_pila((3, 4), ('A', 'B'))}"
    assert package_pila((1, 3, 1), ('L', 'O', 'L')) == ['L', 'O', 'O', 'O', 'L']
test_package_pila()

# def test(s: list[int], c: list[str]) -> list[str]:
#     if not s:
#         return []
#     elif s[0] > 1:
#         return [c[0]] + test([s[0]-1] + s[1:], c)
#     else:
#         return [c[0]] + test(s[1:], c[1:])
#     return ([] if not s else (  [c[0]] + test(list([s[0]-1]) + list(s[1:]), c) if s[0] > 1 else [c[0]] + test(s[1:], c[1:])))
# print(test((5,4,), ('c', 'd')))