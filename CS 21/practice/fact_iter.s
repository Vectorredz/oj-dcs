.data

.text

main:
    li a0, 5 # int n = 10
    mv s0, a0 # copy the argument to s0
    call fact_iter # fact_iter(n)
    
    li a7, 1
    ecall
    # (1) originally ra is here.
    li a7, 10
    ecall

fact_iter:
    # push the ra to the stack hence current ra will be after fact_iter
    addi sp, sp, -16
    sw ra, 12(sp)
    sw s0, 8(sp)
    sw s1, 4(sp)
   
    li s1, 1 # int ret = 1

    li s2, 2 # int k = 2

    call fact_iter_loop # ret (2)
    
    ret
    

fact_iter_loop:
    bgt s2, s0, fact_iter_base # k == n

    mul s1, s1, s2 # ret *= k

    addi s2, s2, 1

    j fact_iter_loop

fact_iter_base:
    mv a0, s1
    j fact_iter_ret # ret (1)

fact_iter_ret:
    lw ra, 12(sp)
    lw s0, 8(sp)
    lw s1, 4(sp)
    addi sp, sp, 16

    ret # ret (1)


