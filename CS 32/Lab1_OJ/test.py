import math

q1 = 6*10**-9
q2 = 8*10**-9
q3 = -10*10**-9

x1 = 3/100
x2 = 5/100
x3 = 3.18/100 # 3.1836

k = 8.99*10**9

f1on3 = abs(k*(q1 * q3) / (x3-x1)**2)
f2on3 = abs(k*(q2 * q3) / (x3-x2)**2)

# print(f1on3)
# print(f2on3)

print(+ f2on3 - f1on3)