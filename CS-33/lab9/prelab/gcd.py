# gcd 

x = 36
y = 20


def gcd(a, b):
    while (b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a // gcd(a, b)) * b

def gcdExtended(a, b, x, y):
    # Base Case 
    if a == 0: 
        x[0] = 0
        y[0] = 1
        return b 

    x1, y1 = [0], [0]
    gcd = gcdExtended(b % a, a, x1, y1)

    # Update x and y using results of 
    # recursive call 
    x[0] = y1[0] - (b // a) * x1[0] 
    y[0] = x1[0] 
    return gcd 

def findGCD(a, b):
    x, y = [1], [1]
    return gcdExtended(a, b, x, y)

def _gcdExtended(a, b, x, y):
    # base case
    if a == 0:
        x[0] = 0
        x[0] = 1
        return b
    
    x1, y1 = [0], [0]
    gcd = _gcdExtended(b % a, a, x1, y1)
    
    x[0] = y1[0] - (b // a) * x1[0]
    y[0] = x1[0]
    return gcd
    
    

def _findGCD(a, b):
    x, y = [1], [1]
    return _gcdExtended(a, b, x, y)

# Main function
def main():
    a, b = 35, 15
    g = findGCD(a, b)
    print(g)

if __name__ == "__main__":
    main()


print(lcm(36, 20))
    



