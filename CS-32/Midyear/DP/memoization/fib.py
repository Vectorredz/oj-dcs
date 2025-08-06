# def fib(n: int) -> int:
#     memo: dict[int, int] = {}
#     if (n in memo):
#         return memo[n]
#     if (n <= 2):
#         return 1
#     else:
#         f = fib(n-1) + fib(n-2)
#         memo[n] = f
#         return f

# print(fib(4))


def fib_iter(n: int):
    fib_list: list[int] = [0]
    fib: int = 1
    memo: dict[int, int] = {}
    for k in range(n):
        if (k in memo):
            fib += memo[k]
        fib = fib + fib_list[k-1]
        fib_list.append(fib)
    return fib
print(fib_iter(15))