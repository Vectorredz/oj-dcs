main:
    addi sp, x0, 0x700
    addi x3, x0, 3
    addi x4, x0, 3
    addi x8, x0, 3
    addi x10, x0, 0
    addi x11, x0, 0
    addi x12, x0, 0
    addi x13, x0, 0
    addi x14, x0, 0

mainloop:
    addi x12, x0, 1
    add x10, x0, x3
    add x11, x0, x4
    beq x0, x0, write_led
after_write_led:
    beq x0, x0, read_keypad
after_read_keypad:
    add x12, x10, x0
    beq x12, x0, move_snake
    add x8, x0, x12

move_snake:
    addi x12, x0, 1
    beq x8, x12, move_snake_up
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

read_keypad:
    to imple
    beq x0, x0, after_read_keypad    

write_led:
    to imple 
    beq x0, x0, after_write_led