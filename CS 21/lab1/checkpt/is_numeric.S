# Checkpoint no. 2: is_numeric.S

.data
buffer: .zero 30
prompt1: .string "INVALID"
prompt2: .string "NUMERIC"
prompt3: .string "NONNUMERIC"

.text
main: 
    call input # call input function
    
    li s0, 0 # int i = 0 // length counter
    li s1, 0 # int flag = 0 // flag is false (non-numeric)
    li s2, 12 # max length 

    call charChecker # call the checker
    
input:
    li a7, 63    # load a7 to read input
    li a0, 0    # load 0 to a0 (stdin)
    la a1, buffer # load the buffer to a1
    li a2, 30    # load 30 bytes as the max length of input
    ecall # call the action
    
    ret 
    
charChecker:
    # access every char in the string
    lb a0, 0(a1) # int *a0 = &a1
    
    addi a1, a1, 1 # a++
    addi s0, s0, 1 # length with spaces

    # numeric character counter
    beq a0, t0, end # end of the string
    bge s0, s2, is_invalid # i > 12
    
    li t1, 48 # ascii for '0'
    li t2, 57 # ascii for '9'
    li t0, 10 # end
    
    # within the bounds
    slt t3, t2, a0 # a0 > 57
    slt t4, a0, t1 # a0 < 48
    xori t3, t3, 1 # a0 <= 57
    xori t4, t4, 1 # a0 >= 48
    and t5, t3, t4 # 48 <= x <= 57
    bnez t5, numeric
    
    # out-of-bounds; if not equal to any numeric value
    blt a0, t1, non_numeric # a0 < 48
    bgt a0, t2, non_numeric # a0 > 57
    
    ecall
    
    j charChecker
    
numeric:
    addi s1, zero, 1 # flag = true (numeric)
    j charChecker
    
non_numeric:
    addi s1, zero, 0 # flag = false (non-numeric)
    j charChecker
    
printNumeric:
    li a7, 4
    la a0, prompt2
    ecall
    j exit

printNonNumeric:
    li a7, 4
    la a0, prompt3
    ecall
    j exit
    
is_invalid:
    li a7, 4
    la a0, prompt1
    ecall
    j exit
    
end:
    bne s1, zero, printNumeric
    beq s1, zero, printNonNumeric
    ecall
  
exit:
    li a7, 10
    ecall