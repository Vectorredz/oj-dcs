def smoothness_param(n: int):
    return (smooth_generator(n) if k_smooth(n, smooth_generator(n)) else None) if n > 1 else 0

def smooth_generator(n: int, k: int = 2) -> int:
    return k if n==1 else smooth_generator(n//k, k) if n % k == 0 else smooth_generator(n, k+1)
    
def k_smooth(n: int, k: int) -> bool:
    return (True if n == 1 else (k_smooth(n//k, k) if n % k == 0 else (k_smooth(n, k-1) if k % 2 == 0 or k == 3 else k_smooth(n, k-2))) if n>1 and k>1 else False)



    
print(smoothness_param(9))

# 280 // 2 = 140
# 140 // 2 = 70
# 70 // 2  = 35
# 35 // 2,3,4,5 = 7
# 7 // 6, 7 = 1