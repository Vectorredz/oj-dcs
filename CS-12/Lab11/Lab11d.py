from __future__ import annotations
import pprint
from collections.abc import Mapping
from dataclasses import dataclass, field

@dataclass
class Directory:
    contents: Mapping[str, File | Directory] = field(default_factory=dict)

@dataclass
class File:
    size: int


# def files_by_size(d: Directory):

#     def path_collector(dir: Directory, path: str, files: list[tuple[str, int]]):
#         for name, item in dir.contents.items():
#             curr_path = f"{path}/{name}" if path else name
#             if isinstance(item, File):
#                 files.append((curr_path, item.size))
#             else:
#                 path_collector(item, curr_path, files)
#     files: list[tuple[str, int]] = []
#     path_collector(d, '', files)
#     return sorted(files, key=lambda x: (x[1], x[0]))

def files_by_size(d: Directory):
    ret: list[tuple[str, Directory | File]] = []
    def path_collector(dir: Directory):
        for name, item in dir.contents.items():
            if isinstance(item, Directory):
                path_collector(item)
            ret.append((name, item))
    path_collector(d)

    return ret

pprint.pp(files_by_size(Directory(contents={
            'basura.txt': File(size=10),
            'Downloads': Directory(contents={
                'basura.txt': File(size=20),
                'basura2.txt': File(size=20),
            }),
            'a.txt': File(size=1500),
            'AA.txt': File(size=1500),
            'Desktop': Directory(contents={
                'lab11': Directory(contents={
                    'cs12232lab11d.py': File(size=500),
                    'test_cs12232lab11d.py': File(size=1500),
                    'basura.txt': File(size=10),
                    'basura2.txt': File(size=10),
                    'sample_input.txt': File(size=200),
                }),
                'basura.txt': File(size=10),
            }),
        })))
# def test_files_by_size():
#     assert files_by_size(Directory(contents={
#             'basura.txt': File(size=10),
#             'Downloads': Directory(contents={
#                 'basura.txt': File(size=20),
#                 'basura2.txt': File(size=20),
#             }),
#             'a.txt': File(size=1500),
#             'AA.txt': File(size=1500),
#             'Desktop': Directory(contents={
#                 'lab11': Directory(contents={
#                     'cs12232lab11d.py': File(size=500),
#                     'test_cs12232lab11d.py': File(size=1500),
#                     'basura.txt': File(size=10),
#                     'basura2.txt': File(size=10),
#                     'sample_input.txt': File(size=200),
#                 }),
#                 'basura.txt': File(size=10),
#             }),
#         })) == [
#             ('Desktop/basura.txt', 10),
#             ('Desktop/lab11/basura.txt', 10),
#             ('Desktop/lab11/basura2.txt', 10),
#             ('basura.txt', 10),
#             ('Downloads/basura.txt', 20),
#             ('Downloads/basura2.txt', 20),
#             ('Desktop/lab11/sample_input.txt', 200),
#             ('Desktop/lab11/cs12232lab11d.py', 500),
#             ('AA.txt', 1500),
#             ('Desktop/lab11/test_cs12232lab11d.py', 1500),
#             ('a.txt', 1500),
#         ]
# test_files_by_size()