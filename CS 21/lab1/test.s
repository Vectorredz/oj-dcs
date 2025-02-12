# Item 2
.data
buffer_x: .zero 30 # s2
intbuffer_x: .zero 30 # s3
buffer_y: .zero 30 # s4
intbuffer_y: .zero 30 # s5

prompt1: .string "enter x: "
prompt2: .string "enter y: "
prompt3: .string "VIVA"
newline: .string "\n"
.text
main_x: 

    # <-------------- process input for x ---------------> #
    li s10, 0 # ouput of x
    li s9, 0 # placeholder variable
    call process_x
    
    # # <-------------- process input for y ---------------> #
    # call process_y
main_y:
    

    li s11, 0 # ouput of y
    li s9, 0 # placeholder variable
    call process_y

main:
    mv s4, s10  # copy the values of x
    mv s5, s11 # copy the values of y
    call gcd

process_x:
    # set s7 as classifier to x 
    # if x == 1 means that it is process x otherwise process y
    li s7, 1

    li a7, 4
    la a0, prompt1
    ecall

    call input_x # call the input
    
    li s0, 0 # int i = 0 
    li s1, 0 # set the int flag = 0 # initialized as false hence non-numeric
    call loadbuffer_x # load the buffer_x
    call charChecker

    ret

process_y:
    # set s7 as classifier to y
    # if x == 0 means that it is process y otherwise process x
    li s7, 0

    li a7, 4
    la a0, prompt2
    ecall

    call input_y # call the input
    
    li s0, 0 # int i = 0 
    li s1, 0 # set the int flag = 0 # initialized as false hence non-numeric
    
    call loadbuffer_y # load the buffer_y
    call charChecker

    ret

input_x:
    # read input from the user
    li a7, 63
    li a0, 0
    la a1, buffer_x # initialize the buffer_x to a1
    li a2, 30 # set max input 

    # initialize the variable for the size of the input
    ecall

    ret

input_y:
 # read input from the user
    li a7, 63
    li a0, 0
    la a1, buffer_y # initialize the buffer_y to a1
    li a2, 30 # set max input 

    # initialize the variable for the size of the input
    ecall

    ret

charChecker:
    # load byte to access the values
    lb s6, 0(s2)

    addi s0, s0, 1 # increment the length
    addi s2, s2, 1 # increment the buffer_x'
    
    # 48 <= a0 <= 57
    li t0, 48 # t0 = 0 
    li t1, 57 # t1 = 9
    li t5, 10 # t5 = ''
    
    slt t2, t1, s6 # a0 > 57
    slt t3, s6, t0 # a0 < 48
    xori t2, t2, 1 # a0 <= 57
    xori t3, t3, 1 # a0 >= 48
    and t4, t3, t2 # 48 <= x <= 57
    bnez t4, is_numeric
    
    beq s6, t5, evaluator # if reach the end of the string
    
    # outside the condition
    blt s6, t0, non_numeric
    bgt s6, t1, non_numeric
    
    j charChecker

# convert the ascii to integer
is_numeric:
    # set the flag to 1
    addi s1, zero, 1 # flag = 1
    j charChecker
    
non_numeric:
    addi s1, zero, 0 # flag = 0
    j charChecker

loadbuffer_x:
    la s2, buffer_x
    la s3, intbuffer_x
    ret 

loadbuffer_y:
    la s2, buffer_y
    la s3, intbuffer_y
    ret  

evaluator:
    # is it numeric or not?
    beqz s1, input_classifier # if non-numeric ask for input again
    bnez s1, loadbuffer_classifier # else convert ascii -> integer

input_classifier:
    # ask for input again because non-numeric
    beqz s7, process_y
    bnez s7, process_x

loadbuffer_classifier:
    beqz s7, bundle_y
    bnez s7, bundle_x

bundle_x:
    call loadbuffer_x
    j iterator_x
bundle_y:
    call loadbuffer_y
    j iterator_y


iterator_x:
    # load the buffer_x again
    lb s6, 0(s2)
    
    addi s2, s2, 1 # iterate again
    
    li t0, 10
    
    beq s6, t0, output_classifier
    beq s6, zero, output_classifier
    
    call converter_classifier
    
    
    j iterator_x

iterator_y:
    # load the buffer_y again
    lb s6, 0(s2)
    
    addi s2, s2, 1 # iterate again
    
    li t0, 10
    
    beq s6, t0, output_classifier
    beq s6, zero, output_classifier
    
    call converter_classifier
    
    
    j iterator_y
    
converter_classifier:
    beqz s7, converter_y
    bnez s7, converter_x

converter_x:
    addi s6, s6, -48 # convert ascii to integer
    sb s6, 0(s3) # store the converted ascii to the intbuffer_x
    call formatInteger
    
    addi s3, s3, 1
    
    j iterator_x

converter_y:
    addi s6, s6, -48 # convert ascii to integer
    sb s6, 0(s3) # store the converted ascii to the intbuffer_x
    call formatInteger
    
    addi s3, s3, 1
    
    j iterator_y


output_classifier:
    beqz s7, store_y
    bnez s7, store_x

store_x:
    mv s10, s9 # overwrites the buffer
    j main_y

store_y:
    mv s11, s9 # overwrites the buffer
    j main


formatInteger:
    li t0, 10 #a
    mul s9, s9, t0
    add s9, s9, s6 # s9 is the final integer for that call 
    ret

gcd: 
    li s8, 0
    beqz, s11, is_relprime
    rem t0, s10, s11
    add s10, zero, s11
    add s11, zero, t0

    j gcd

# iterate over the gcd
output: 
    li a7, 4
    la a0, prompt3
    ecall

    j end


is_relprime:
    li t0, 1
    beq s10, t0, output

    bne s10, t0, factorization


factorization:
    li a7, 1

    addi s8, s8, 1
    
    rem t0, s4, s8 # s4 % i == 0
    xori t0, t0, 1 # == 1
    rem t1, s5, s8 # s5 % i == 0
    xori t1, t1, 1 # == 1
    and t2, t1, t0 # divisible both

    mv a0, s8
    ecall 

    beq s8, s4, end

    j factorization

    /*
    for (int i = 0; i < s10; i++){
        if (s4 % i == 0 && s5 % i == 0){
            print(i)
        }
    }
    */

printNewLine:
    la a0, newline
    li a7, 4
    ecall
    jr x1
end:
 # print outs
    li a7, 10
    ecall
    
    




