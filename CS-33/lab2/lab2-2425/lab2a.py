# implement OrderedSet
from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class Node:
    val: int
    l: "Node | None" = None
    r: "Node | None" = None
    
def contains(node: Node | None, val):
    if (node is None): return None
    assert node is not None
    
    if (node.val > val):
        return contains(node.l, val)

class PokemonTeam:
    def __init__(self, initial_team: Sequence[tuple[int, int]]):
        ...
    def add(self, i: int, l: int):
        ...
    def remove(self, i: int):
        ...
    def sum(self, i: int, j: int) -> int:
        ...