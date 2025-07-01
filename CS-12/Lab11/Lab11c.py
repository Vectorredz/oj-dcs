from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar, Callable

T = TypeVar('T')

@dataclass(frozen=True)
class Branch(Generic[T]):
    value: T
    children: tuple[Branch[T], ...] = ()

def trim(is_bad: Callable[[T], bool], branch: Branch[T]) -> Branch[T] | None:
    return None if is_bad(branch.value) else Branch(branch.value, trim_none(tuple(trim(is_bad, ch) for ch in branch.children)))
    
def trim_none(children: tuple[Branch[T] | None, ...]) :
    return tuple(ch for ch in children if ch != None)

def is_bad1(value: int) -> bool:
    return not (50 <= value <= 100)

tree = Branch(value=69, children=(
        Branch(value=80, children=(
            Branch(value=80),
            Branch(value=10),
            Branch(value=69),
        )),
        Branch(value=20),
        Branch(value=70),
        Branch(value=120, children=(
            Branch(value=60),
        )),
    ))

print(trim(is_bad1, tree))