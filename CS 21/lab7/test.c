#include <stdio.h>
#include <stdlib.h>

/*
int main(){
    int base = 0xf000000;
    int on = 0xfffffff
    for (int i = 0; i < 8; i++){
        mem[base] = on;
        base += 4
        mem[base] = off
    }
}
 
lui x1 0xf0000 # base = 0xf000000
lui x2 0xfffff # on = 0xfffffff
ori x2 x2 0xfff

addi x3 zero 0 # i = 0
addi x4 zero 8 # i = 8
mv x5 x1

L1: bge x3 x4 L2 # i >= 8
    sw x2 0(x1)
    addi x1 x1 4
    addi x3 x3 1
    j L1
# reset
L2: addi x3 x3 0 #
    mv x1 x5 # reset base
    j L3
L3: bge x3 x4 L4
    sw x5 0(x1)
    addi x1 x1 4
    addi x3 x3 1
    j L3
L4: nop


lui x1 0xf0000 # base = 0xf000000
lui x2 0xfffff # on = 0xfffffff
ori x2 x2 0xfff
mv x5 x1

sw x2 0(x1)
sw x5 0(x1)



*/