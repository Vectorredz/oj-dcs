main:
    # initialize registers
    addi sp, x0, 0x700 # SP
    addi x3, x0, 3 # rows
    addi x4, x0, 3 # cols
    addi x8, x0, 3 
    # return values
    addi x10, x0, 0 # x10
    addi x11, x0, 0 # x11

    # functions
    addi x12, x0, 0 # x12 if pressed
    addi x13, x0, 0  # x13 # row
    addi x14, x0, 0 # x14 # col
    

mainloop:
    # sets x12 to 1 
    # set the initial rows and cols
    # jumps to led
    addi x12, x0, 1 # x12 = 1 # to RDsl
    add x10, x0, x3 # x10 = 3 # starts with row3
    add x11, x0, x4 # x11 = 3 # starts with col3
    # call write_led(x10: row = 3, x11: col = 3, x12: move = 1)
    
    beq x0, x0, write_led

after_write_led:
    # call read_keypad(x10: row = 3, x11: col = 3, x12: move = 1)
    beq x0, x0, read_keypad

after_read_keypad:
    # call move_snake(x10: row = 3, x11: col = 3, x12: move = 3)

    add x12, x10, x0 
    beq x12, x0, move_snake # x12 stores on which keypad pressed
    add x8, x0, x12

move_snake:
    # call move_snake_up(x10: row = 3, x11: col = 3, x12: move = 4)

    addi x12, x0, 1 
    beq x8, x12, move_snake_up # if equal means key pressed
    beq x0, x0, after_move_snake_up
move_snake_up:
    addi x13, x0, -1
    addi x14, x0, 0
after_move_snake_up:
    addi x12, x0, 2
    beq x8, x12, move_snake_down
    beq x0, x0, after_move_snake_down
move_snake_down:
    addi x13, x0, 1
    addi x14, x0, 0
after_move_snake_down:
    addi x12, x0, 3
    beq x8, x12, move_snake_left
    beq x0, x0, after_move_snake_left
move_snake_left:
    addi x13, x0, 0
    addi x14, x0, -1
after_move_snake_left:
    addi x12, x0, 4
    beq x8, x12, move_snake_right
    beq x0, x0, after_move_snake_right
move_snake_right:
    addi x13, x0, 0
    addi x14, x0, 1
after_move_snake_right:
    add x3, x3, x13
    add x4, x4, x14

    beq x0, x0, mainloop


up:
    addi a0 x0 1
    beq x0 x0 after_read_keypad
    
down:
    addi a0 x0 2
    beq x0 x0 after_read_keypad
    
left:
    addi a0 x0 3
    beq x0 x0 after_read_keypad
    
right:
    addi a0 x0 4
    beq x0 x0 after_read_keypad

read_keypad:
    # call write_led(x10: row = 3, x11: col = 3, x12: move = 1)
    lw x18 0x300(x0)

    addi x19 x0 1
    
    addi x20 x0 2

    addi x21 x0 4
    
    addi x22 x0 8

    # x18 == x19 -> move up
    beq x18 x19 up
    # x18 == x20 -> move down
    beq x18 x20 down
    # x18 == x21 -> move left
    beq x18 x21 left
    # x18 == x22 -> move right
    beq x18 x22 right

    beq x0, x0, after_read_keypad  


write_led:
    # on the led
    slli x15, x10, 4     
    slli x16, x10, 2
    lw x17 0x200(x0)
    add x15, x15, x11
    addi x15, x15, 0x200    # x15 = final address (base + offset)
    sw x12, 0(x15)        

    beq x0, x0, after_write_led

