# def symmetry_cost(s: str) -> int:
#   return (0 if s == '' else (1 + symmetry_cost(s[1:-1]) 
#             if s[0] != s[-1] else symmetry_cost(s[1:-1])))

# print(symmetry_cost('BANANA'))

def fibonacci(s: int) -> int:
  if s == 0:
    return 0
  elif s == 1 or s == 2:
    return 1
  else:
    return fibonacci(s-1) + fibonacci(s-2)
  

print(fibonacci(5))

# 0 1 1 2 3 5 8 13