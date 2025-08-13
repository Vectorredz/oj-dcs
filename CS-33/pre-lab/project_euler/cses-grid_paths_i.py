# set the base case

# def grid_paths():
def parse_grid(str_grid: str):
    rows = []
    clean = list(filter(lambda x: x != '\n', str_grid))
    for i in range(0,len(clean),4):
        if (i % 4 == 0):
            rows.append(clean[i:i+4])
    print(rows)   
    

str_grid: str = """
....
.*..
...*
*...
"""
# 0->3
# 4->7
# 8->11
# 12->15
parse_grid(str_grid)