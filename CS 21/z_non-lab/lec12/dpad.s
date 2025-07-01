lui x1 0xf000
addi x2 x2 -1

addi x3 x3 1 // row
addi x4 x4 1 // col

slli x6 x3 5
slli x7 x4 2
add x8 x6 x7
add x9 x1 x8

sw x2 0(x9)

# polling
lui x10 0xf0000
ori x10 x10 100

l1: 
    beq x10 x2 end
loop: 
    beq x0 x0 l1

end:
    li a7 1
    mv a0 x2
    ecall

#define D_PAD_0_BASE (0xf0000100)
#define D_PAD_0_SIZE (0x10)
#define D_PAD_0_UP_OFFSET (0x0)
#define D_PAD_0_UP (0xf0000100)
#define D_PAD_0_DOWN_OFFSET (0x4)
 
#define D_PAD_0_LEFT_OFFSET (0x8)
#define D_PAD_0_LEFT (0xf0000108)
#define D_PAD_0_RIGHT_OFFSET (0xc)
#define D_PAD_0_RIGHT (0xf000010c)