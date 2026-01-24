def simplex(A, b, c):
    EPS = 1e-9
    m = len(A)
    n = len(c)

    # 1. build tableau
    width = n + m + 1
    height = m + 1
    T = [[0.0] * width for _ in range(height)]

    # 2. fill constraints and slacks
    for i in range(m):
        for j in range(n):
            T[i][j] = float(A[i][j])
        T[i][n + i] = 1.0
        T[i][-1] = float(b[i])

    # 3. fill the objective row (we use -c for maximization)
    for j in range(n):
        T[m][j] = -float(c[j])

    # 4. pivot operation
    def pivot(r, s):
        piv = T[r][s]
        inv = 1.0 / piv
        # normalize pivot row
        for j in range(width):
            T[r][j] *= inv
        # eliminate pivot column from other rows
        for i in range(height):
            if i != r and abs(T[i][s]) > EPS:
                factor = T[i][s]
                for j in range(width):
                    T[i][j] -= factor * T[r][j]

    # simplex main loop
    while True:
        s = None
        min_value = -EPS
        # entering variable: most negative coefficient in last row
        for j in range(width - 1):
            if T[m][j] < min_value:
                min_value = T[m][j]
                s = j
        if s is None:
            break  # optimal

        # leaving variable: min ratio test
        r = None
        best = float('inf')
        for i in range(m):
            if T[i][s] > EPS:
                ratio = T[i][-1] / T[i][s]
                if ratio < best - EPS:
                    best = ratio
                    r = i

        if r is None:
            # unbounded
            return None, None

        pivot(r, s)

    # extract solution: only accept columns that are exact unit vectors
    x = [0.0] * n
    tol = 1e-9
    for j in range(n):
        pivot_row = None
        for i in range(m):
            if abs(T[i][j] - 1.0) < tol:
                # ensure all other entries in column are ~0
                ok = True
                for k in range(m):
                    if k != i and abs(T[k][j]) > tol:
                        ok = False
                        break
                if ok:
                    pivot_row = i
                    break
        if pivot_row is not None:
            x[j] = T[pivot_row][-1]
        else:
            x[j] = 0.0

    optimal_value = T[m][-1]
    return optimal_value, x

# test the example
A = [
    [1, 3, 2],
    [1, 5, 1]
]
b = [10, 8]
c = [8, 10, 7]

val, sol = simplex(A, b, c)
print(val, sol)  # prints: 64.0 [8.0, 0.0, 0.0]
