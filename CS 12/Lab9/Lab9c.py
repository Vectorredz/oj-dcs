from typing import Sequence

def powersets(s: str):
    powerset = ([s[i:] for i in range(len(s)+1)])
    sorted_powerset = sorted(powerset)
    k = list(map(lambda x : len(powerset)-1 if not x else powerset.index(x) , sorted_powerset))
    return k
print(powersets("banana"))


def k_mapping(s: str, powerset: list[str], sorted_powerset: list[str]) -> list[int]:
    return ([] if not sorted_powerset else 
            ([powerset.index(sorted_powerset[0])] + k_mapping(s, powerset, sorted_powerset[1:]) if powerset.index(sorted_powerset[0]) else 
             ([0] + k_mapping(s, powerset, sorted_powerset[1:]) if sorted_powerset[0] == s else k_mapping(s, powerset, sorted_powerset[1:]) ))
             )
def powerset(s: str)-> list[str]:
    return [''] if not s else [s[:]] + powerset(s[1:])

def insert(elem: str, sorted_elems: Sequence[str]) -> list[str]:
    return ([elem] if not sorted_elems else [elem] + list(sorted_elems) 
                if elem < sorted_elems[0] else [sorted_elems[0]] + insert(elem, sorted_elems[1:]))

def insertion_sort(elems: Sequence[str]) -> list[str]:
    return [] if not elems else insert(elems[0], insertion_sort(elems[1:]))

def suffix_array(s: str):
    return k_mapping(s, powerset(s), insertion_sort(powerset(s)))
print(suffix_array('banana'))