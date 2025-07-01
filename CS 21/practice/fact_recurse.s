.data
/*
int fact_rec(int n) {
  if (n <= 0) {
    return 1;
  }
 
  return n * fact_rec(n - 1);
}
*/
.text
main:
    li s0, 5          # n = 5
    mv a0, s0         # int n = 5
    
    call fact_rec     # fact_rec(a0 = 5)

    # <- ra

    li a7, 1          # Print integer
    ecall

    li a7, 10         # Exit program
    ecall

fact_rec:
    # push
    addi sp, sp, -8  # Allocate space for ra, a0, and s0
    sw ra, 4(sp)
    sw s0, 0(sp)      # Save s0
    
    ble a0, zero, fact_rec_base # (n <= 0) return fact_ret

    mv s0, a0         # s0 = n
    addi a0, a0, -1   # (n-1)

    call fact_rec     # fact_rec(n-1)

    mul t0, s0, a0    # n * fact_rec(n-1)
    mv a0, t0

    j fact_rec_ret

fact_rec_base:
    li t0, 1
    mv a0, t0 
    
    j fact_rec_ret

fact_rec_ret:
    lw ra, 4(sp)
    lw s0, 0(sp)
    addi sp, sp, 8# Deallocate stack space
    ret

