def fastest_resilience(n_0: int) -> int:
    # % 10 gets the last digit
    # //10 removes the last digit
    
    if (n_0 < 0):
        return 0
    else:
        max_digit: float | int = float('-inf')
        dn_0 = n_0
        # get the max digit
        while (dn_0):
            curr_digit = dn_0 % 10    
            if (curr_digit >= max_digit):
                max_digit = curr_digit
            dn_0 //= 10
        
        n_0 -= (max_digit**2)
        return 1 + fastest_resilience(n_0)
print(fastest_resilience(12))
