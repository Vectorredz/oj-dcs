# Item 2
.data
buffer: .zero 30
prompt: .string "enter: "

.text
main: 
    li a7, 4
    la a0, prompt
    ecall

    call inputUser # call the input
    
    li s0, 0 # int i = 0 
    li s1, 0 # set the int flag = 0 // initialized as false hence non-numeric
    call charChecker

inputUser:
    # read input from the user
    li a7, 63
    li a0, 0
    la a1, buffer # initialize the buffer to a1
    li a2, 30 # set max input 

    # initialize the variable for the size of the input
    ecall

    ret

charChecker:
    # load the buffer
    # load byte to access the values
    li a7, 11
    lb a0, 0(a1)
    
    addi s0, s0, 1 # increment the length
    addi a1, a1, 1 # increment the buffer'
    
    # 48 <= a0 <= 57
    li t0, 48 # t0 = 48
    li t1, 57 # t1 = 57
    
    slt t2, a0, t0 # t2 = a0 < t0
    xori t2, t2, 1 # t2 = a0 >= t0
    slt t3, t1, a0 # t3 = a0 > t1
    xori t3, t3, 1 # t3 = a0 <= t1
    and t4, t3, t2 # t4 = t3 && t2
    
    bnez t4, is_numeric # t4 != 0 hence t4 = 1; numeric
    beq a0, zero, end # if reach the end of the string

    ecall
    
    j charChecker

# convert the ascii to integer
is_numeric:
    addi a1, a1,
    # set the flag to 1
    li s1, 1
    ret
    
end:
    li a7, 1
    mv a0, s1
    ecall
    li a7, 10
    ecall
    
    




