# Laboratory Report 1: Item 1 - read_int.S

# registers

.data
buffer: .zero 30
newline: .string "\n"

.text
main: 
    call input # call input function

    li s0, 0 # int i = 0
    li s1, 10 # int x = 10; maxLength
    li s2, 0 # int z = 0; resultingInteger

    call loopBuffer # call the copyBuffer function and accept s0, s1, s2, s3
    
input:
    li a7, 63    # load a7 to read input
    li a0, 0    # load 0 to a0 (stdin)
    la a1, buffer # load the buffer to a1
    li a2, 30    # load 30 bytes as the max length of input
    ecall # call the action
    
    ret 

loopBuffer:
    lb a0, 0(a1) #  int *a0 = &a1

    li s3, 45 # ascii of '-'
    li s4, 48 # ascii of '0'
    li s5, 57 # ascii of '9'
    li s6, 10 # ascii of '\n'
    
    addi a1, a1, 1 # a1++
    
    # within the bounds (0-9)
    slt t0, s5, a0 # a0 > 57
    slt t1, a0, s4 # a0 < 48
    xori t0, t0, 1 # a0 <= 57
    xori t1, t1, 1 # a0 >= 48
    and t2, t0, t1 # 48 <= a0 <= 57

    bnez t2, copyBuffer
    
    beq a0, s3, loopBuffer # skip the '-'
    beq a0, s6, doubleInteger 
    beq s0, s1, doubleInteger # if s0 == s1 j double

    ecall

    j loopBuffer    

copyBuffer:
    addi a0, a0, -48 # convert the character from ascii to integer

    addi s0, s0, 1 # track the length of the buffer

    # format the integer
    call formatInteger
    
    beq s0, s1, doubleInteger # if s1 == s0 j double

    j loopBuffer
    
formatInteger:
    # result = 0
    # result = 0 * 10 + 1
    # result = 1 * 10 + 2
    # result = 12 * 10 + 3
    li t0, 10
    mul s2, s2, t0
    add s2, s2, a0
    
    ret

printNewLine:
    li a7, 4
    la a0, newline
    ecall
    ret
    
doubleInteger:
    li t0, 2
    mul s2, s2, t0
    j end
    
end:
    li a7, 1
    mv a0, s2
    ecall
    li a7, 1
    mv a0, s0
    ecall
    
