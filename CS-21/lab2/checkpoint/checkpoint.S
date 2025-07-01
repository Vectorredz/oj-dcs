.text
main:
    li s0, 1 # let the input be the value passed to s0
    mv a0, s0 # copy a0 to s0
    call f # call the function f
    
    # (ret1) print call
    li a7, 1 
    ecall
    
    # end call
    li a7, 10
    ecall

f:
  # push 
  addi sp, sp, -8 # allocate memory for the stack
  sw ra, 0(sp) # store the return address to be at (ret1)
  sw s0, 4(sp) # store the n
  
  mv s0, a0 # copy a0 to s0
  
  # if n <= 0 return 0
  ble a0, zero, f_ret_base
  addi a0, s0, -1 # (n-1)
  
  call f # f(n-1)
  call f # f(f(n-1))
  sub a0, s0, a0 # n - f(f(n-1))
  j f_ret # jump to the ret function

f_ret_base:
  addi a0, zero, 0 # return 0
  j f_ret # jump to pop the allocated memory
  
f_ret:
  # pop 
  lw ra, 0(sp)
  lw s0, 4(sp)
  addi sp, sp, 8
  ret # return to the caller (ret1)
