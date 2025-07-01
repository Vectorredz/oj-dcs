
# def powerset(s: str):
#     subsets: list[str] = ['']
#     for elem in s:
#         k = [elem + sets for sets in subsets]
#         subsets.extend(k)
#     return subsets
# print(powerset('banana'))

# arr = 'banana'
# ret = [i for i in arr]
# print(ret)

def generating_powersets(arr: str, i: int = 0, curr: list[str] = []) -> list[list[str]]:
    return [curr] if i == len(arr) else generating_powersets(arr, i + 1, curr + [arr[i]]) + generating_powersets(arr, i + 1, curr)

# def generating_powersets(s: str) -> list[str]:
#     return [''] if not s else generating_powersets(s[1:]) + [s[0] + subset for subset in generating_powersets(s[1:])]

def len_map(powersets: list[list[str]], k: int) -> list[list[str]]:
    return [] if not powersets else [powersets[0]] + len_map(powersets[1:], k) if len(powersets[0]) == k else len_map(powersets[1:], k)

def num_distinct_subseqs(s: str, k: int):
    return remove_dupes(len_map(generating_powersets(s, 0), k))

def remove_dupes(powersets: list[list[str]]) -> int:
    return 0 if not powersets else 1 + remove_dupes(powersets[1:]) if powersets.count(powersets[0]) == 1 else remove_dupes(powersets[1:])

print(num_distinct_subseqs('banana', 0))