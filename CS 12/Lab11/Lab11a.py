from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    children: Sequence[Person] = ()

def count_matching_names(person: Person):
    same_name: list[str] = []
    def people(peep: Person):
        nonlocal same_name
        first_letter = person.name[0]
        for child in peep.children:
            if peep.name[0] == first_letter:
                same_name.append(peep.name)
            people(child)
    people(person)
    return same_name

print(count_matching_names(Person(name='tom', children=(
            Person(name='tom'),
            Person(name='toom'),
            Person(name='thomas', children=(
                Person(name='charlie'),
                Person(name='tim'),
            ))))))

    