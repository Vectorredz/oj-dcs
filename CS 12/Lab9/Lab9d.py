# def k_smooth()
# def is_prime(n: int, k:int = 2) -> list[int]:
#     return [] if k > n else [k] + is_prime(n//k, k) if n % k == 0 else is_prime(n, k+1)

def k_smooth(n: int, k: int) -> bool:
    # if n > 1 and k > 1:
    #     if n == 1:
    #         return True
    #     elif n % k == 0:
    #         return k_smooth(n//k, k)
    #     else:
    #         if k % 2 == 0 or k == 3:
    #             return  k_smooth(n, k-1)
    #         else:
    #             return k_smooth(n, k-2)
    # else:
    #     return False

    return (True if n == 1 else (k_smooth(n//k, k) if n % k == 0 else (k_smooth(n, k-1) if k % 2 == 0 or k == 3 else k_smooth(n, k-2))) if n>1 and k>1 else False)


    
print(k_smooth(560, 6))

def prime_factors(n: int):
    factors: list[int] = []
    k = 2
    # for _ in range(n):
    #     if n % k == 0:
    #         n = n // k
    #         factors.append(k)
    #     else:
    #         k += 1
    # return factors
    while k <= n:
        if n % k == 0:
            n //= k
            factors.append(k)
        else:
            k += 1
    return factors



# w
