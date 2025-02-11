def f(n):
    if (n <= 0):
        return 0
    return n - f(f(n-1))
for i in range(16):
    print(i, f(i))