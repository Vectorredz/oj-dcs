# Laboratory Report 2: Item 2 - relprime.S

.data
buffer_x: .zero 30 
intbuffer_x: .zero 30 
buffer_y: .zero 30 
intbuffer_y: .zero 30 
prompt3: .string "VIVA"
newline: .string "\n"

.text
main_x: 
    # <-------------- process input for x ---------------> #
    li s10, 0 # output of x
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

    # checks if x < y or x >= y
    slt t0, s10, s11  # if x < y, need to swap x and y
    beqz t0, gcd       # if x >= y, jump to the gcd
    mv t1, s10         # swap: t1 = x
    mv s10, s11        # x = y
    mv s11, t1         # y = t1 
    call gcd

process_x:
    # set s7 as classifier to x 
    # if x == 1 means that it is process x otherwise process y
    li s7, 1

    call input_x # call the input
    
    li s0, 0 # int i = 0 
    li s1, 0 # set the int flag = 0 # initialized as false hence non-numeric
    call loadbuffer_x # load the buffer_x
    call charChecker # call the charChecker to check every single input

    ret

process_y:
    # set s7 as classifier to y
    # if x == 0 means that it is process y otherwise process x
    li s7, 0

    call input_y # call the input
    
    li s0, 0 # int i = 0 
    li s1, 0 # set the int flag = 0 # initialized as false hence non-numeric
    
    call loadbuffer_y # load the buffer_y
    call charChecker # call the charChecker to check every single input

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
    bnez t4, is_numeric # once the character is within the boundary 
    
    beq s6, t5, evaluator # if reach the end of the string
    
    # outside the condition
    blt s6, t0, is_non_numeric # 
    bgt s6, t1, is_non_numeric # 
    
    j charChecker # jump to charChecker again iterate the loop

# convert the ascii to integer
is_numeric:
    # set the flag to 1
    addi s1, zero, 1 # int flag = 1
    j charChecker
    
is_non_numeric:
    addi s1, zero, 0 # int flag = 0
    j charChecker

loadbuffer_x:
    # 
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
    # identify which buffer to load 
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
    # determine where to store the output depending on the current input
    beqz s7, store_y # jump to store_y to store the entered y input 
    bnez s7, store_x # jump to store_x to store the entered x input 

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
    beq s10, t0, output # if the output is 
    bne s10, t0, factorization

printNewLine:
    la a0, newline
    li a7, 4
    ecall
    ret

factors: 
    li a7, 1 
    mv a0, s8
    ecall 
    call printNewLine
    j factorization

factorization:
    li t5, 13
    addi s8, s8, 1
    
    rem t0, s4, s8 # s4 % i == 0
    rem t1, s5, s8 # s5 % i == 0
    or t2, t1, t0 # divisible both

    beq s8, t5, end
    beqz t2, factors

    j factorization
    
end:
 # print outs
    li a7, 10
    ecall
    
    