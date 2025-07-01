import sys
sys.setrecursionlimit(69696969)

def function(x):
  if x >= 40: return 1
  y = x+1
  return function(y+(function(y+1)))


print(function(3))