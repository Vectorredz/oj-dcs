
w: int = 40
values: list[int] = [10, 20, 30, 40]
weights: list[int] = [30, 10, 40, 20]

items: dict[int, int] = {weights[i]: values[i] for i in range(len(weights))}

total_subset: list[list[int]] = []
def generate_subset(num: list[int]):
    curr_subset: list[int] = []
        
    # dfs to the array
    def dfs(i: int):
        if (i >= len(num)):
            return total_subset.append(curr_subset.copy())
        
        else: 
            # include append to the curr_subset
            dfs(i + 1)
            curr_subset.append(num[i])
            # exclude pop to the curr_subset
            dfs(i + 1)
            curr_subset.pop()
            
            return total_subset
        
    # for i in range(len(num)):
    #     dfs(i)
    return dfs(0)

print(generate_subset([1,2,3]))
        
        
        
        
    
    



# generate_subset([1,2,3])

















# res: list[list[int]] = []
# def generate_subset(num: list[int]):
    
#     subset: list[int] = []
#     # [10, 20, 30, 40]
#     def dfs(i: int):
#         if (i >= len(num)):
#             res.append(subset.copy())
#             return res
        
#         else:
#             # include in the subset
#             subset.append(num[i]) # [10]
#             dfs(i+1)

#             # exclude from the subset
#             subset.pop() # []
#             dfs(i+1)
            
#             return res
    
#     return dfs(0)

# def knapsack(items: dict[int ,int]):
#     total_weight: int = 0 
#     max_value: int = 0
#     for num in generate_subset(weights):
#         v: list[int | None] = []
#         total_weight = sum(num)
#         curr_value: int = 0 
#         if (total_weight <= w): # consider only combination of weights that are below the threshold
#             # check if these values yields the maximum value
#             for i in num:
#                 curr_value += items[i]
#                 v.append(items.get(i))
#             if (curr_value >= max_value):
#                 max_value = curr_value
#                 yield list(v)[-1]
                
#     yield max_value                    
# print(*knapsack(items=items))

                
            
    


        
