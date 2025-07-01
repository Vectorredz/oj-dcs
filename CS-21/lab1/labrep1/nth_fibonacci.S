# Laboratory Report 3: Item 3 - nth_fibonacci.S

.data
newline: .string "\n"
buffer: .zero 30
intBuffer: .zero 30

.text
main:
    call askInput # call to ask for inputs
    
    call loadBuffers # call to load the buffers
    li s0, 0 # flag for negative numeric // int flag = false
    li s1, 0 # length of the input; how many digits in a number
    li s2, 0 # flag for is_numeric // int flag = false
    li s3, 0 # digit accumulator
    call inputChecker # call to check every character in the input

askInput:
    li a7, 63 # read input
    li a0, 0 # stdin
    la a1, buffer # the input will be stored in a1
    li a2, 30

    ecall

    ret 

loadBuffers:
    la a1, buffer # let a0 be the pointer to a1
    la a3, intBuffer # let a2 be the pointer to a3
    ret

inputChecker:
    lb a0, 0(a1) # int *a0 = &a1
    
    addi a1, a1, 1 # a1++ 

    li t0, 10 # ascii of ''
    li t1, 48 # ascii of '0'
    li t2, 57 # ascii of '9'
    li t6, 45 # ascii of '-'

    # check if the char is within the boundaries
    slt t3, a0, t1 # a1[i] < 48
    xori t3, t3, 1 # a1[i] >= 48
    slt t4, t2, a0 # a1[i] > 57
    xori t4, t4, 1 # a1[i] <= 57
    and t5, t3, t4 # 48 <= a1[i] <= 57
    
    # terminating conditions
    beq a0, s7, validator # a1[i] == ''

    # numeric
    bnez t5, is_numeric

    # check for negative numeric 
    beq a0, t6, signed_flag

    # non-numeric 
    blt a0, t1, is_non_numeric # a1[i] < 0
    bgt a0, t2, is_non_numeric # a1[i] > 9
    
    j inputChecker

signed_flag:
    li s0, 1 # let flag = 1 if the input entered is negative
    j inputChecker

is_numeric:
    li t0, -48
    addi a0, a0, -48 # convert to integer

    sb a0, 0(a3) # int *a0 = &a3

    call formatInteger

    addi s1, s1, 1 # increment the length
    addi a2, a2, 1 # increment the array to access new element 
    
    li s2, 1 # set flag to true
    
    j inputChecker

is_non_numeric:
    li s2, 0 # set flag to false
    
    j inputChecker

negateInteger:
    li t0, -1 
    mul a0, a0, t0 # multiply the final integer to -1 to negate
    j negated
    
    
formatInteger:
    li t0, 10 
    mul s3, s3, t0 # 0 * 10
    add s3, s3, a0 # 0 * 10 + 1
    
    ret

validator:
    # check if the integer passed is negative
    mv a0, s3
    bnez s0, negateInteger
    
    negated:
    # copy the negated/positive s3 to the register

    li t0, 1
    li t1, 2
    li t2, 0
    li t3, 0
    
    slt t3, t2, a0 # 0 < a0
    xori t3, t3, 1 # 0 >= a0
    bnez t3, end
    beq a0, t0, printZero # num == 1
    beq a0, t1, printOne # num == 2

    li s0, 0 # int a = 0
    li s1, 1 # int b = 1
    li s2, 0 # int fibn

    li s3, 3 # int i = 0
    j fibonacci

fibonacci:
    li a7, 1
    
    add s2, s0, s1 # fibn = a + b
    mv s0, s1 # a = b
    mv s1, s2 # b = fibn
    
    addi s3, s3, 1 # i++;
    bgt s3, a0, printFibn # s3 > a0 
    j fibonacci


printFibn:
    li a7, 1
    mv a0, s2
    ecall
    j end

printZero:
    li a7, 1
    li a0, 0
    ecall
    j end

printOne:
    li a7, 1
    li a0, 1
    ecall
    j end
    
end:
    li a7, 10
    ecall


