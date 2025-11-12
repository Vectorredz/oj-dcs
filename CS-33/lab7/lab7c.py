from oj import optimal_assignment
from collections.abc import Sequence
def min_energy(p,b,d,must_carry,must_be_carried,e):
    inf=10**14
    c=set(must_carry); f=set(must_be_carried); k=max(d,len(c),len(f))
    if k>min(p,b): return None
    n=p+b-k
    if n == 0: return 0
    a=[[inf]*n for _ in range(n)]
    for i in range(p,n):
        for j in range(b):
            a[i][j]= 0 if j not in f else inf
        for j in range(b,n):
            a[i][j]= 0
    for i in range(p):
        for j in range(b):
            t = e[i][j]; a[i][j]= t if t is not None else inf
        for j in range(b,n):
            if i not in c:
                a[i][j] = 0 
            else:
                a[i][j] = inf
    return None if (ret := optimal_assignment(a)) is None or ret>=inf else ret
