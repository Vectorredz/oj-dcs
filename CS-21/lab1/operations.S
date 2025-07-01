.data
prompt: .string "Enter: "


.text
main:
    # sum
    li s0, 0xf # s0 = 15
    li s1, 10 # s1 = 10
    li s2, 0 # init s2
    add s2, s0, s1 # s2 = s0 + s1
    
    # difference
    li s1, -10 # s1 = -10
    li s3, 0
    add s3, s0, s1 # 
    
    # product
    li s1, 10
    li s4, 0
    mul s4, s0, s1
    
    # quotient
    li s5, 0
    div s5, s0, s1
    
    # remainder
    li t0, 0
    rem t0, s0, s1
    
    # AND
    li s6, 0
    and s6, s0, s1
    
    # NAND
    li s6, 0
    and s6, s0, s1
    xori, s6, s6, 1
    
    # XNOR
    and t0, s0, s1
    xori t1, t1, 1
    or t2, t0, t1
    
    # OR
    li s7, 0
    or s7, s0, s1
    
    # NOR
    li s7, 0
    or s7, s0, s1
    xori, s7, s7, 1
    
    # XOR
    li s8, 0
    xor s8, s0, s1
    
    # NOT
    xori, t0, t1, 1
    
    
    
    
    
    
    