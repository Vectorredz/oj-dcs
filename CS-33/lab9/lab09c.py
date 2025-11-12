from collections.abc import Sequence

def _gcd(a, b):
    a, b = abs(a), abs(b) # force to be positive
    if b == 0:
        return a
    return _gcd(b, a % b)
def refine_split(option):
    factors = set(option)
    changed = True
    while changed:
        changed = False
        list_factors = list(factors)
        new = set()
        for x in list_factors:
            split = False
            for y in list_factors:
                g = _gcd(x, y)
                if 1 < g < x:
                    new.add(g)
                    new.add(x // g)
                    changed = True
                    split = True
                    break
            if not split:
                new.add(x)
        factors = new
    return factors          
def find_decomposition(f: Sequence[int]) -> tuple[list[int], list[list[int]]]:
    f, n = [int(x) for x in f], len(f)
    if n == 0:
        return [], []
    if all(x == 1 for x in f):
        return [], [ [] for _ in f ]
    option = set()
    for i in range(n):
        for j in range(i+1, n):
            g = _gcd(f[i], f[j])
            if g > 1:
                option.add(g)
    if not option:
        g_list = [x for x in f]
        vectors = []
        for i in range(n):
            vec = [0]*n
            vec[i] = 1
            vectors.append(vec)
        return g_list, vectors

    while True:
        option = refine_split(option)   
        cands_list = sorted(option)     
        remains = f[:]  
        exps = [[0]*len(cands_list) for _ in range(n)]
        for idx, c in enumerate(cands_list):
            for i in range(n):
                k = 0
                while remains[i] % c == 0:
                    remains[i] //= c
                    k += 1
                exps[i][idx] = k

        new_rems = set(r for r in remains if r > 1)
        added = False
        # build matrix
        for r in new_rems:
            if r not in option:
                option.add(r)
                added = True
        if not added:
            g_list = sorted(option)
            a = []
            for i in range(n):
                row = []
                x = f[i]
                for g in g_list:
                    k = 0
                    while x % g == 0:
                        x //= g
                        k += 1
                    row.append(k) # exponent power
                a.append(row)
            return g_list, a
