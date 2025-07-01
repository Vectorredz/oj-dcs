/*
<--------------- 1. SIMPLE FUNCTION CALL ----------------->
'''
int main() 
{
    simple();
    a = b + c;
}

void simple()
{
    return;
}
'''

/*
<-------------- 1. RISC-V SIMPLE FUNCTION ----------------->
'''
main: 
    jal simple # PC 0x30000000
    addi a, b, c # PC 0x30000004

simple:
    jal ra # PC 0x30000004
'''

Call Function: Jump and link (jal function):

- CALLER essentialy LINKS the PC to PC + 4 so once called jal function it will set the return address to PC + 4

Return from Function: Jump Register (jr ra):

- once called, will do operation. After jr ra to JUMP to the linked address by the CALLEE

=> CALLER:
    - passes arguments to the callee
    - jumps to callee   

=> CALLEE:
    - performs the function
    - returns result to caller
    - returns to point of call
    - must not overwrite register or memory 
*/


/*
<--------------- 2. DIFFERENCE OF SUMS ----------------->
'''
int main()
{
    int y;
    ...
    y = diffofsums(2,3,4,5);
    ...
}

int diffofsums(int f, int g, int h, int i)
{
    int result; 
    result = (f + g) - (h + i);
    return result

}

'''

<------------- 2. RISC-V DIFFERENCE OF SUMS -------------->

'''
main: 
    li s0, 0

    li a0, 2 # f
    li a1, 3 # g
    li a2, 4 # h
    li a3, 5 # i

    jal diffofsums

    li a7, 1
    mv a0, a0

    ecall


diffofsums:
    li t3, -1 # for subtracting

    add t1, a0, a1 # t1 = a0 + a1
    add t2, a2, a3 # t2 = a2 + a3
    mul t2, t2, t3 # -t2
    add a0, t1, t2

    jr ra
'''

*/

#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);

    if (num <= 0){
        return 0;
    } else if (num == 1){
        printf("0");
        return 0;
    } else if (num == 2){
        printf("1");
        return 0;
    }

    int a = 0;
    int b = 1;
    int fibn;

    for (int i = 3; i <= num; i++) {
        fibn = a + b;
        a = b;
        b = fibn;
    }

    printf("%d",fibn);
}