lui s0 0xf0000
addi s1 s1 -1
addi s2 s2 4
addi s3 s3 2
addi t1 t1 8
addi t2 t2 36
addi s5 s5 36

loop:
    bge t3 t1 end
    
    beq t3 x0 if
    bne t3 x0 else
    if:
        sw s1 0(s0)
        addi t3 t3 1
        beq x0 x0 loop
        
    else:
        add s6 s0 t2
        sw s1 0(s6)
        add t2 t2 s5
        addi t3 t3 1
        beq x0 x0 loop
    
end:
    nop