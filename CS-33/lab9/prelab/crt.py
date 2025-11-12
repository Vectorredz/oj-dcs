# x = 2 mod 3
# x = 3 mod 5
# x = 2 mod 7
# xi = a mod b
"""
1. find M
M = b1 x b2 x b3
  = 3 x 5 x 7
  
2. find m1, m2, m3
mi = M / bi

3. do extended gcd 
yi = Mi % bi

4. do the 
x = SUM(yi bi ai) mod M 
"""