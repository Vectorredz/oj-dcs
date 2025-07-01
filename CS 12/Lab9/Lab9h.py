def days_of_war(s1: int, s2: int, s3: int, s4: int, s5: int) -> int:
    return  0 if min(s1, s2, s3, s4, s5) == 0 else \
            1 + days_of_war(s1 - min(s2, s3, s4,s5), s2, s3, s4, s5) \
            if max(s1, s2, s3, s4, s5) == s1 else \
            1 + days_of_war(s1, s2 - min(s1, s3, s4,s5), s3, s4, s5) \
            if max(s1, s2, s3, s4, s5) == s2 else \
            1 + days_of_war(s1, s2, s3 - min(s1, s2, s4,s5), s4, s5) \
            if max(s1, s2, s3, s4, s5) == s3 else \
            1 + days_of_war(s1, s2, s3, s4  - min(s1, s2, s3,s5), s5) \
            if max(s1, s2, s3, s4, s5) == s4 else \
            1 + days_of_war(s1, s2, s3, s4, s5 - min(s1, s2, s3,s5)) 
       