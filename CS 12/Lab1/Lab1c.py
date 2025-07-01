from typing import TypeVar
import pprint
T = list[list[int]]

def grid_transforms(M: T, inst: list[str]) -> list[T]:
    rows, cols = len(M), len(M[0])
    M_copy = M[:]
    ret_matrix_h = [[0]*cols for _ in range(rows)]
    ret_matrix_v = [[0]*rows for _ in range(cols)]
    ret_matrix = []

    def flip_v():
        nonlocal M
        for row in range(rows):
            ret_matrix_h[row] = M[row][::-1]
    
    def flip_h():
        nonlocal M, ret_matrix_h
        ret_matrix_h = M[::-1]

    def flip_se():
        nonlocal M, ret_matrix_v
        for row in range(rows):
            for col in range(cols):
                ret_matrix_v[col][row] = M[row][col]

    def flip_ne():
        nonlocal M, ret_matrix_v
        for row in range(rows):
            for col in range(cols):
                ret_matrix_v[::-1][col][row] = M[::-1][row][col]

    def move_d():
        nonlocal M_copy, M
        d = M_copy.pop(0)
        M_copy.append(d)

    def move_r():
        nonlocal ret_matrix_h, M_copy
        for row in range(rows):
            r = M[row].pop(0)
            M_copy[row].append(r)

    def rotate_cw():
        nonlocal ret_matrix_v
        for row in range(rows):
            for col in range(cols):
                ret_matrix_v[col][row] = M[::-1][row][col]
    
    def rotate_ccw():
        nonlocal ret_matrix_v
        for row in range(rows):
            for col in range(cols):
                ret_matrix_v[::-1][col][row] = M[row][col]

        
    for command in inst:
        if command == "FLIP_V":
            flip_v()
            ret_matrix.append(ret_matrix_h)
        if command == "FLIP_H":
            flip_h()
            ret_matrix.append(ret_matrix_h)
        if command == "FLIP_SE":
            flip_se()
            ret_matrix.append(ret_matrix_v)
        if command == "FLIP_NE":
            flip_ne()
            ret_matrix.append(ret_matrix_v)
        if command == "MOVE_D":
            move_d()
            ret_matrix.append(M_copy)
        if command == "MOVE_R":
            move_r()
            ret_matrix.append(M_copy)
        if command == "ROTATE_CW":
            rotate_cw()
            ret_matrix.append(ret_matrix_v)
        if command == "ROTATE_CCW":
            rotate_ccw()
            ret_matrix.append(ret_matrix_v)

    return ret_matrix
pprint.pp(grid_transforms(
    [
        [11, 12, 21, 22],
        [98, 89, 99, 88],
        [73, 37, 33, 77],
    ],
    ["ROTATE_CCW"]
))
