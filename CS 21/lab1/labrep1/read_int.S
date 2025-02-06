# Laboratory Report 1: Item 1 - read_int.S

.data
buffer: .zero 30
intbuffer: .zero 10
newline: .string "\n"

.text
main: 
    call input # call input function
    
    call loadBuffers # initialize the buffers into s registers

    li s3, 0 # int i = 0
    li s4, 10 # x = 10; maxLength
    li s9, 0 # result = 0

    call loopBuffer # call the copyBuffer function and accept s0, s1, s2, s3
    
input:
    li a7, 63    # load a7 to read input
    li a0, 0    # load 0 to a0 (stdin)
    la a1, buffer # load the buffer to a1
    li a2, 30    # load 30 bytes as the max length of input
    ecall # call the action
    
    ret 

loadBuffers:
    la s0, buffer # load the buffer to s0
    la s1, intbuffer # load the intbuffer to s1

    ret # return s0, s1 to main

loopBuffer:
    lb s8, 0(s0) #  load byte buffer to s8 to access values

    li t1, 45 # ascii of '-'
    li t2, 48 # ascii of '0'
    li t3, 57 # ascii of '9'
    li t4, 10 # ascii of '\n'
    
    addi s0, s0, 1 # s0 + 1 to access the next element
    
    # within the bounds (0-9)
    slt s5, t3, s8 # s8 > 57
    slt s6, s8, t2 # s8 < 48
    xori s5, s5, 1 # s8 <= 57
    xori s6, s6, 1 # s8 >= 48
    and s7, s5, s6 # 48 <= s8 <= 57
    bnez s7, copyBuffer
    
    beq s8, t1, loopBuffer # skip the '-'
    beq s8, t4, doubleInteger
    beq s3, s4, doubleInteger # if s3 == s4 j double

    ecall

    j loopBuffer    

copyBuffer:
    addi s8, s8, -48
    sb s8, 0(s1) #  load s8 to s1
    addi s3, s3, 1 # track the length of the buffer
    
    li a7, 1
    mv a0, s8

    ecall

    # format the integer
    call formatInteger
    
    addi s1, s1, 1 # s1 + 1 to access the next element
    
    beq s3, s4, doubleInteger # if s3 == s4 j double

    j loopBuffer
    
formatInteger:
    li t0, 10
    mul s9, s9, t0
    add s9, s9, s8
    
    ret

printNewLine:
    li a7, 4
    la a0, newline
    ecall
    ret
    
doubleInteger:
    li t0, 2
    mul s9, s9, t0
    j end
    
end:
    call printNewLine
    li a7, 1
    mv a0, s9
    ecall
    
