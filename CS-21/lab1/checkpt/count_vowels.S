# Checkpoint no. 1: count_vowels.S

.data
buffer: .zero 30  # set the buffer to max 30 bytes with zeroes       

.text
main:
    call inputStart        # Call the function to enter input

    # call the function to check every single vowel in the entered string (uppercase and lowercase)
    li s0, 0 # int counter = 0
    call checkVowel

inputStart:
    li a7, 63             # syscall to read input (string)
    li a0, 0              # stdin
    la a1, buffer         # load buffer address to a1
    li a2, 30           # set max input size to a2 = 30
    ecall                 # start the input 
    
    ret                   # return to main
    
checkVowel:
    li t0, 10        # end of string
    # lowercase vowels
    li t1, 97        # vowel: 'a'
    li t2, 101        # vowel: 'e'
    li t3, 105        # vowel: 'i'
    li t4, 111        # vowel: 'o'
    li t5, 117       # vowel: 'u'
    
    # uppercase vowels
    li s1, 65        # vowel: 'A'
    li s2, 69        # vowel: 'E'
    li s3, 73        # vowel: 'I'
    li s4, 79        # vowel: 'O'
    li s5, 85       # vowel: 'U'
    
    lb a0, 0(a1) # access the val at *buffer
    addi a1, a1, 1 # *buffer + 1 
 
    beq a0, zero, endChar # if reached the end of the string
    
    # Checks if the encountered character is a vowel
    
    # lowercase vowels
    beq a0, t1, counter 
    beq a0, t2, counter 
    beq a0, t3, counter 
    beq a0, t4, counter
    beq a0, t5, counter
    
    # uppercase vowels
    beq a0, s1, counter 
    beq a0, s2, counter 
    beq a0, s3, counter
    beq a0, s4, counter 
    beq a0, s5, counter
    
    ecall
    
    j checkVowel
    
counter:
    addi s0, s0, 1 # update the vowelCounter 
    ecall
    j checkVowel
    
endChar:
    li a7, 1
    mv a0, s0 # print the vowel counted
    ecall
    
    li a7, 10 # end the program
    ecall
    