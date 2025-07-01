#include <stdio.h>
#include <stdlib.h>

unsigned int compute_passcode(unsigned int a0){ // a0 = 202312019
    unsigned int a5 = 0; // sw a5, -20(s0)
    unsigned int  a4 = a0; // lw a5, -36(s0)
    for (unsigned int  i = 0; 2 >= i; i++){ // bge a5, a4, ret
        a5 = a4 >> (i + 5);
        /*
        lw a5, -20(s0) -> a5 = i
        addi a5, a5, 5 -> a5 = i + 5
        lw a4, -36(s0) -> a4 = student_number
        srl a5, a4, a5 -> a5 = a4 >> a5
        lw a4, -36(s0) -> a4 = student_number
        */
        a5 = a5 ^ a4;
        a4 = a5;
        a5 = (0x27d4f << 12) - 1235;
        /*
        xor a5, a5, a4 -> a5 ^ a4
        t0 = a5 
        a4 = t0
        addi a5, a5, -1235
        */
        a5 = a4 * a5;
        a4 = a5;
        /*
        mul a5, a4, a5
        t0 = a5
        a5 = i
        a5 = (i + 1)
        t1 = a5
        a4 = t1
        */  
    }
    return a5;

}

int main(){
    unsigned int student_number;
    scanf("%u", &student_number);
    printf("%u ",   compute_passcode(student_number));
}