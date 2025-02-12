
.text
main:
    li a0, 10 # pass int n = 10
    call fact_iter # a0 = 10

    li a7, 1      # print
    ecall
    
    li a7, 10      # exit
    ecall

fact_iter:
    li s0, 1 # int ret = 1
    li s1, 2 # int k = 2

    # push to the stack 
    addi sp, sp -12
    sw ra, 8(sp) # store the return address now
    sw s0, 4(sp)
    sw s1, 0(sp)


    call fact_iter_loop

    mv a0, s0 # copy the return value to a0 <- this is the point of return
    ret


fact_iter_loop:
    bgt s1, a0, fact_iter_ret
    mul s0, s0, s1
    addi s1, s1, 1
    j fact_iter_loop

fact_iter_ret:

    lw s1, 0(sp)
    lw s0, 4(sp)
    lw ra, 8(sp)
    addi sp, sp, 8

    ret
