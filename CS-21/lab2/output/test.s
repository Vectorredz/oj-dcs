main:
    li s0, 3 # x = 3
    mv a0, s0 
    li s1, 0 # init y
    call function # function(x)
function:
    addi sp, sp, -12
    sw ra, 0(sp)
    sw s0, 4(sp)
    sw s1, 8(sp)

    li t0, 40
    bge a0, t0, function_base

    addi s1, a0, 1 # y = x + 1
    mv a0, s1 # x = y new param

    call function # function ( y + 1)
    addi a0, s1, a0 # y + function(y+1)

    call function # function(y + function(y+1))

    j function_ret


function_base:
    li t0, 0
    mv a0, t0
    j function_ret

function_ret:
    lw ra, 0(sp)
    lw s0, 4(sp)
    lw s1, 8(sp)
    addi sp, sp, 12

    ret

  
  