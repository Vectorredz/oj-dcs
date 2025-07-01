.data
msg: .string ". hello world\n"

.text
    li s0, 1 # int i = 0
    li s1, 4 # int x = 3
    loop:
        beq s0, s1, end     # if (i > 3)

        li a7, 1             # print i
        mv a0, s0         # load i into s0
        ecall             # call the os to do a7 command
        
        li a7, 4
        la a0, msg
        ecall
        
        addi s0, s0, 1
        jal loop

    end:
        li a7, 10
        ecall
