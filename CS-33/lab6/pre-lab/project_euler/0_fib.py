from typing import Callable
import sys
sys.setrecursionlimit(2000) # Set a higher limit, adjust as needed

def cache(func):
    memo: dict[int, int] = {}
    def cached_func(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return cached_func


# Top to bottom - MEMOIZATION
memo: dict[int, int] = {} 

@cache
def fibonacci(n: int) -> int:
    if (n == 0):
        return 0
    if (n <= 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# # Bottom up - Dynamic Programming

# def fibonacci(n: int):
#     dp: list[int | None] = [None] * (n+1)
#     for i in range(len(dp)):
#         if (i == 0):
#             dp[i] = 0
#         elif (i <= 2):
#             dp[i] = 1
#         else:
#             dp[i] = dp[i-1] + dp[i-2]
#     # return dp[n]
#     print(dp[n])


print(fibonacci(1000))