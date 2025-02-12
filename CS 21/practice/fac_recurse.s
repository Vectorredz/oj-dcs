.text
main:
    li a0, 4         # Pass n = 4
    call fact_rec    # Call factorial function

    # Exit program
    li a7, 1         # Syscall for print
    ecall

    li a7, 10        # Exit
    ecall

fact_rec:
    mv s0, a0        # Save n in s0
    mv t0, s0        # Copy n into t0 for later use

    # Push ra and s0 to the stack
    addi sp, sp, -8
    sw ra, 4(sp)      # Save return address
    sw s0, 0(sp)      # Save argument (n)

    blez s0, fact_rec_base  # Base case: if n <= 0, return 1

    addi s1, s0, -1   # n - 1
    mv a0, s1         # Pass n-1 as argument to the next recursive call
    call fact_rec     # Recursive call: fact_rec(n-1)

    # After returning from fact_rec(n-1), multiply result by n
    lw s0, 0(sp)      # Restore the original n
    mul a0, a0, s0    # Multiply result by n (a0 = fact_rec(n-1) * n)

fact_rec_ret:
    # Restore saved registers
    lw ra, 4(sp)      # Restore return address
    lw s0, 0(sp)      # Restore argument (n)
    addi sp, sp, 8    # Pop the stack

    ret               # Return to caller

fact_rec_base:
    li a0, 1          # Base case: return 1 if n <= 0
    j fact_rec_ret    # Jump to return sequence