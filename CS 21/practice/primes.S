.data
prompt: .string "enter: "
prompt1: .string "prime"
prompt2: .string "not a prime"
buffer: .zero 30

.text
main:
    call userInput
    
    li s11, 0 # finalInteger
    li s10, 2 # for looping
    call loopBuffer


userInput:
    li a7, 63
    li a0, 0
    la a1, buffer
    li a2, 30

    ecall
    
    ret

loopBuffer:
    lb a0, 0(a1) # int *a0 = &a1

    li s0, 10 # '-'
    li s1, 48 # '0'
    li s2, 57 # '9'

    addi a1, a1, 1 # increment the buffer

    # check conditions if wihtin the bounds (0-9)
    # 48 <= a0 <= 57
    slt t0, a0, s1 # a0 < 48
    xori t0, t0, 1 # a0 >= 48
    slt t1, s2, a0 # a0 > 57
    xori t1, t1, 1 # a0 <= 57
    and t2, t0, t1 # 48 <= a0 <= 57

    bnez t2, is_numeric
    
    beq a0, t0, is_prime

    j loopBuffer

is_numeric:
    # convert ascii to integer
    addi a0, a0, -48 # integer

    call formatInteger

    j loopBuffer

formatInteger:
    # 123
    # 0 * 10 + 1 = 1
    # 1 * 10 + 2 = 12
    # 12 * 10 + 3 = 123
    mul s11, s11, s0 # 0 * 10  
    add s11, s11, a0 # 0 * 10 + 1

    ret

is_prime:
    
    li s3, 1
    li s4, 2
    li s5, 3

    li a2, 5

    # if (num <= 1) return 0;
    blt s11, s3, end
    beq s11, s4, prime
    beq s11, s5, prime

    rem t0, s11, s4
    beq t0, zero, end

    rem t1, s11, s5
    beq t1, zero, end

    j loop_prime

    # if (num == 2 || num == 3) return 1;
    # if (num % 2 == 0) return 0;
    # if (num % 3 == 0) return 0;
    # for (int i = 5; i * i <= num; i++){
    #     if (num % i == 0 || num % (i + 2) == 0){
    #         return 0;
    #     }
    # }
    # return 1;
loop_prime:

    addi a2, a2, 1 # increment 
    rem t2, s11, a2

    beqz t2, end

    beq a2, t2, prime

    j loop_prime

prime:
    li a7, 4
    la a0, prompt1
    ecall
    
    j exit

prime_factorization:

    /*

    FOR:    bge i, num, endFOR
            addi i, i, 2
            call WHILE
    
    WHILE:  beq num, i, endWHILE
            j WHILE

    endWHILE:
            j FOR

    endFOR:
        j end

    */


    
    

end:
    li a7, 4
    la a0, prompt2
    ecall
    
    j exit

exit: 
    li a7, 10
    ecall