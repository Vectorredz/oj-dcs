capacity: int = 7
weights: list[int] = [3,2,4,5,1]
values: list[int] = [50,40,70,80,10]
inventory: list[int] = []

def knapsack_dp(c: int, weights: list[int], values: list[int]):
    # create w * v matrix
    r: int = len(weights)
    matrix: list[list[int]] =[[0 for _ in range(c + 1)]for _ in range(r + 1)]
    memo: dict[int, int] = {}
    for row in range(r + 1):
        for col in range(c + 1):
            # set the edges to 0
            dr: int = row - 1
            if (row == 0 or col == 0) and row <= r:
                matrix[row][col] = 0
            elif (row <= r):
                if (weights[dr] <= col):
                    
                    matrix[row][col] = values[dr]
                    # apply the current weight
                    col_weight: int = col
                    curr_weight: int = col - weights[dr]
                    
                    curr_val: int = 0
                    
                    # same item
                    if (matrix[dr][curr_weight] == values[dr]):
                        curr_val = values[dr]
                    else:
                        curr_val = values[dr] + matrix[dr][curr_weight] 
                    
                    matrix[row][col] = max(curr_val, matrix[dr][col])
                else:
                    matrix[row][col] = matrix[dr][col]
    
    # find the values
    
    # start the pivot from the last eleemnt
    pivot: int = matrix[r][c]
    pivot_col: int = c
    for row in range(r, -1, -1):
        for col in range(c , -1, -1):
            dr: int = row - 1
            if (pivot == matrix[dr][col] and (col == pivot_col and pivot > 0)):
                continue
            elif (pivot != matrix[dr][col] and (col == pivot_col and pivot > 0)):
                # add the pivot to the inventory
                inventory.append(row)
                # update pivot
                pivot -= values[dr]
            
    print(inventory)
            
                
    

    # for mat in matrix:
    #     print(mat)
    # print(memo)
    
knapsack_dp(capacity, weights, values)