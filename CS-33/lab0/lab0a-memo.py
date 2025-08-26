
import time
def fastest_resilience(n_0: int) -> int:
    # % 10 gets the last digit
    # //10 removes the last digit
    memo: dict[int, int] = {}
    def dfs(n_0: int) -> int | float:d
        minimum: int | float = float('inf')
        # time.sleep(0)
        if (n_0 in memo):
            return memo[n_0]
        if (n_0 <= 0):
            memo[n_0] = 0
            return 0
        else:
            for i in list(map(lambda x: int(x), str(n_0))):
                if (i != 0):
                    dn_0 = n_0 - i**2
                    path = 1 + dfs(dn_0)
                    if (path < minimum):
                        minimum = path
            memo[n_0] = minimum
            return memo[n_0]
    
    x = dfs(n_0)
    return x

for i in range(300):
    print(i,  fastest_resilience(i))