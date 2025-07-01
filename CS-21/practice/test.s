.text
main:
    li a0, 10        # n = 10
    call sum_iter    # call iterative sum function

    li a7, 1      # exit
    ecall
    
    li a7, 10      # exit
    ecall

sum_iter:
    li s0, 0         # sum = 0
    li s1, 1         # k = 1

    # push registers onto the stack
    addi sp, sp, -12
    sw ra, 8(sp)     # save return address
    sw s0, 4(sp)     # save s0 (sum)
    sw s1, 0(sp)     # save s1 (k)

    call sum_iter_loop

    mv a0, s0        # move result to a0

    # restore registers
    lw s1, 0(sp)
    lw s0, 4(sp)
    lw ra, 8(sp)
    addi sp, sp, 12  # deallocate stack space

    ret

sum_iter_loop:
    beq s1, a0, sum_iter_ret  # if k > n, return
    add s0, s0, s1            # sum += k
    addi s1, s1, 1            # k++
    j sum_iter_loop

sum_iter_ret:
    ret