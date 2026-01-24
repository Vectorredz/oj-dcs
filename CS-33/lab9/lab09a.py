from collections.abc import Sequence
def count_feastable_subsequences(a: Sequence[int]) -> int:
    n: int = len(a)
    l: int = (max(a) + 1)
    dp: list[int] = [0] * l
    ret = 0
    # [0, 1, 2, 3, 4, 5, 6]
    for i, x in enumerate(a):
        dp[x] += 1
        for d in range(x, l, x):
            dp[d] += dp[x]

    for i in a:
        ret += dp[i]
    print(ret)
    return ret % 998244353

count_feastable_subsequences((1, 3, 2, 6))
