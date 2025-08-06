"""
1. convert first the string in an array
2. r = 25, c = 13
two pass
1. first iteration traverse the grid to find the start
2. second iteration do the dfs traversal




"""


def can_reach_end(r: int, c: int, grid: str) -> bool:
    return True

# def _find_start(r: int, c: int, grid: str) -> tuple[int, int]:
#     for row in range(r):
#         for col in range(c):
#             if 
#     return 

def _convert_to_array(r: int, c: int, grid: str):
    i = 0
    for row in range(0, r * c, 13):
        print(grid[row: row+13], row, row+13)

grid: str =  """\
#############

#   #   #   #

# X #   #   #

#   #   #   #

###### ######

#   #   #   #

#           #

#   #   #   #

## ##########

#   #   #   #

#         S #

#   #   #   #

#############"""
_convert_to_array(26,13,grid)


print()