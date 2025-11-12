"""
input: 1, n
output: primes from 1 -> n

1. set the base case

"""
from math import sqrt

def sieve(n: int):
    is_primes: list[bool] = [True for _ in range(n + 1)]
    pf: list[list[int]] = [[] for _ in range(n + 1)]
    # set the base case
    is_primes[0] = is_primes[1] = False
    [0,1,2,3,4,5]
    # 1. loop thru n and check if 2i, 3i, 5i, 7i are is_primes
    for d in range(2, n):
        if is_primes[d]:
            for i in range(2, n):
                di = d * i
                if di < n:
                    is_primes[di] = False
                else:
                    break
        # else:
        #     num = d
        #     for i in range(2, n):
        #         while (num):
        #             if num % i == 0:
        #                 pf[d].append(i)
        #                 num //= i
        #             else: break
    print(pf)


sieve(100)
