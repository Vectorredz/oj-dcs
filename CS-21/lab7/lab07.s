main:
    # initialize registers
    addi sp, x0, 0x700 # SP
    addi x3, x0, 3 # snake-x
    addi x4, x0, 3 # snake-y
    addi x8, x0, 3 # current dir

    # return values
    addi x10, x0, 0 # a0
    addi x11, x0, 0 # a1

    # functions
    addi x12, x0, 0 # a2 
    addi x13, x0, 0  # a3 : rows
    addi x14, x0, 0 # a4 : cols
    

mainloop:
    # sets x12 to 1 
    # set the initial rows and cols
    # jumps to led
    addi x12, x0, 1 # x12 = 1 # update led
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
    lw x15 0x300(x0)

    addi x16 x0 1
    
    addi x17 x0 2

    addi x18 x0 4
    
    addi x19 x0 8

    # x15 == x16 -> move up
    beq x15 x16 up
    # x15 == x17 -> move down
    beq x15 x17 down
    # x15 == x18 -> move left
    beq x15 x18 left
    # x16 == x19 -> move right
    beq x15 x19 right

    beq x0, x0, after_read_keypad  


write_led:
    # on the led
    slli x6, x10, 6      # 
    slli x7, x11, 2       # 
    add x5, x6, x7        # x5 = (row * 16) + (column * 4)
    addi x5, x5, 0x200    # x5 = final address (base + offset)
    sw x12, 0(x5)        

    beq x0, x0, after_write_led

