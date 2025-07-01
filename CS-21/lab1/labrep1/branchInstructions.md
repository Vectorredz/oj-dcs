# Laboratory 1 
## Item 4 - Branch Pseudoinstructions

<details>
<summary>Branch Greater Than Or Equal (bge)</summary>
<hr>

The non-pseudoinstructions used to implement `bge` is the following:
- `slt` - Set Less Than
- `xori` - XOR immediate
- `beq` - Branch Equal to

Suppose you have two (2) registers `s0` and `s1` . In this example we can demonstrate how `bge` is used:


```
<------- Using BGE -------->

bge s0, s1, <label>
```
This instruction checks if `s0` is greater than or equal `s1` then it will branch/jump out to the `label` passed otherwise, move to the next instruction.

```
<------- Implementing BGE -------->

# load the registers first

li s0, 0 # int a = 0
li s1, 0 # int a = 0
li t0, 0 # int x = 0
li t1, 1 # bool true

slt t0, s0, s1 # s0 < s1
xori t0, t0, 1 # s0 >= s1 
beq t0, t1, <label> # t0 == 1 
```
1. We first load the registers to `zero` for initialization.
2. Compare `s0` and `s1` using `slt` instruction to create `s0 < s1`
3. Store the evaluation to a temporary register `t0`.
4. Using the non-pseudoinstruction `xori` we negate `t0` register to get `>=`. Hence, `t0` now contains the evaluation of `s0 >= s1`
5. To determine if `t0` is evalued to `true` we pass `t0` to `beq` a non-pseudoinstruction that compares two (2) registers, then jumps if true otherwise go to next instruction. 
   - We pass in `t1` register that is hardcoded to `1` which acts as (`boolean`) true if `t0` evaluation satisfies the condition. 

### USE EXAMPLE 
#### testcases: 
- s0 = 1, s1 = 2
- s0 = 1, s1 = 1
- s0 = 2, s1 = 1

Notice that both implementation yields to the same answers and thus, not limited to the testcases. Thereby, validating that `bge` can be implemented with only (3) pseudoinstructions

Using `bge`
```

.data
prompt1: .string "'s0' is greater than or equal to `s1`"
prompt2: .string "`s0` is not greater than or equal to `s1`"


.text
main:
    li s0, 1 # int a = 1
    li s1, 2 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    # slt t0, s0, s1 # s0 < s1 
    # xori t0, t0, 1 # s0 >= s1 
    # beq t0, t1, out1
    
    bge s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```


Using `non-pseudoinstruction implementation`
```
testcases: 
s0 = 1, s1 = 2
s0 = 1, s1 = 1
s0 = 2, s1 = 1

.data
prompt1: .string "'s0' is greater than or equal to `s1`"
prompt2: .string "`s0` is not greater than or equal to `s1`"


.text
main:
    li s0, 1 # int a = 1
    li s1, 2 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    slt t0, s0, s1 # s0 < s1 
    xori t0, t0, 1 # s0 >= s1 
    beq t0, t1, out1
    
    # bge s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```

 QED.
</details>

<details>

<summary>Branch Greater Than Or Equal Unsigned (bgeu) </summary>
<hr>
Similar to the first item, we can make use of other non-pseudoinstructions. 

The non-pseudoinstructions used to implement `bgeu` is the following:
- `sltu` - Set Less Than Unsigned
- `xori` - XOR immediate
- `beq` - Branch Equal to

Instead of using `slt` we are just going to use `sltu` which stands for Set Less Than Unsigned. It is an instruction that performs an unsigned comparison between two registers and sets the destination register to 1 if the first operand is less than the second, otherwise, it sets the destination to 0.


```
<------- Using BGEU -------->

bgeu s0, s1, <label>
```
This instruction treats the registers `s0` and `s1` as unsigned. It checks if `s0` is greater than or equal `s1` then it will branch/jump out to the label passed otherwise, move to the next instruction.

```
<------- Implementing BGEU -------->

# load the registers first

li s0, 0 # int a = 0
li s1, 0 # int a = 0
li t0, 0 # int x = 0
li t1, 1 # bool true

sltu t0, s0, s1 # s0 < s1
xori t0, t0, 1 # s0 >= s1 
beq t0, t1, <label> # t0 == 1 
```
1. We first load the registers to `zero` for initialization.
2. Compare `s0` and `s1` using `sltu` instruction to create `s0 < s1`
3. Store the evaluation to a temporary register `t0`.
4. Using the non-pseudoinstruction `xori` we negate `t0` register to get `>=`. Hence, `t0` now contains the evaluation of `s0 >= s1`
5. To determine if `t0` is evalued to `true` we pass `t0` to `beq` a non-pseudoinstruction that compares two (2) registers, then jumps if true otherwise go to next instruction. 
   - We pass in `t1` register that is hardcoded to `1` which acts as (`boolean`) true if `t0` evaluation satisfies the condition. 

### USE EXAMPLE 
#### testcases: 
- s0 = -1, s1 = -2
- s0 = -1, s1 = -1
- s0 = -2, s1 = -1

Notice that both implementation yields to the same answers and thus, not limited to the testcases. Thereby, validating that `bgeu` can be implemented with only (3) pseudoinstructions

Using `bgeu`
```

.data
prompt1: .string "'s0' is greater than or equal to unsigned `s1`"
prompt2: .string "`s0` is not greater than or equal to unsigned `s1`"

.text
main:
    li s0, -1 # int a = -1
    li s1, -2 # int b = -2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    # sltu t0, s0, s1 # s0 < s1 
    # xori t0, t0, 1 # s0 >= s1 
    # beq t0, t1, out1
    
    bgeu s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```


Using `non-pseudoinstruction implementation`
```
testcases: 
s0 = -1, s1 = -2
s0 = -1, s1 = -1
s0 = -2, s1 = -1

.data
prompt1: .string "'s0' is greater than or equal to unsigned `s1`"
prompt2: .string "`s0` is not greater than or equal to unsigned `s1`"


.text
main:
    li s0, -1 # int a = -1
    li s1, -2 # int b = -2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    sltu t0, s0, s1 # s0 < s1 
    xori t0, t0, 1 # s0 >= s1 
    beq t0, t1, out1
    
    # bgeu s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```

 QED.



</details>

<details>

<summary>Branch Less than (blt)</summary>
<hr>

The non-pseudoinstructions used to implement `blt` is the following:
- `slt` - Set Less Than Unsigned
- `beq` - Branch Equal to


```
<------- Using BLT -------->

blt s0, s1, <label>
```
This instruction checks if `s0` is less than `s1` then it will branch/jump out to the label passed otherwise, move to the next instruction.

```
<------- Implementing BLT -------->

# load the registers first

li s0, 0 # int a = 0
li s1, 0 # int a = 0
li t0, 0 # int x = 0
li t1, 1 # bool true

slt t0, s0, s1 # s0 < s1
beq t0, t1, <label> # t0 == 1
```
1. We first load the registers to `zero` for initialization.
2. Compare `s0` and `s1` using `slt` instruction to create `s0 < s1`
3. Store the evaluation to a temporary register `t0`.
4. To determine if `t0` is evaluated to `true` we pass `t0` to `beq` a non-pseudoinstruction that compares two (2) registers, then jumps if true otherwise go to next instruction. 
   - We pass in `t1` register that is hardcoded to `1` which acts as (`boolean`) true if `t0` evaluation satisfies the condition. 
 

### USE EXAMPLE 
#### testcases: 
- s0 = 1, s1 = 2
- s0 = 1, s1 = 1
- s0 = 2, s1 = 1

Using `blt`
```
.data
prompt1: .string "'s0' is not less than 's1'"
prompt2: .string "'s0' is less than 's1'"

.text
main:
    li s0, 2 # int a = 1
    li s1, 3 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    # slt t0, s0, s1 # s0 < s1 == 1
    # beq t0, t1, out2
    
    blt s0, s1, out2
    
    j out1

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```
Using `non-pseudoinstruction implementation`

```
.data
prompt1: .string "'s0' is not less than 's1'"
prompt2: .string "'s0' is less than 's1'"

.text
main:
    li s0, 2 # int a = 1
    li s1, 3 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    slt t0, s0, s1 # s0 < s1 == 1
    beq t0, t1, out2
    
    # blt s0, s1, out2
    
    j out1

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```
QED.
</details>

<details>

<summary>Branch Less Than Unsigned (bltu)</summary>
<hr>

The non-pseudoinstructions used to implement `bltu` is the following:
- `sltu` - Set Less Than Unsigned
- `beq` - Branch Equal to


```
<------- Using BLT -------->

bgeu s0, s1, <label>
```
This instruction treats `s0` and `s1` as unsigned. It checks if `s0` less than `s1` then it will branch/jump out to the label passed otherwise, move to the next instruction.

```
<------- Implementing BLT -------->

# load the registers first

li s0, 0 # int a = 0
li s1, 0 # int a = 0
li t0, 0 # int x = 0
li t1, 1 # bool true

sltu t0, s0, s1 # s0 < s1
beq t0, t1, <label> # t0 == 1
```
1. We first load the registers to `zero` for initialization.
2. Compare `s0` and `s1` using `sltu` instruction to create `s0 < s1`
3. Store the evaluation to a temporary register `t0`.
4. To determine if `t0` is evaluated to `true` we pass `t0` to `beq` a non-pseudoinstruction that compares two (2) registers, then jumps if true otherwise go to next instruction. 
   - We pass in `t1` register that is hardcoded to `1` which acts as (`boolean`) true if `t0` evaluation satisfies the condition. 
 

### USE EXAMPLE 
#### testcases: 
- s0 = 1, s1 = 2
- s0 = 1, s1 = 1
- s0 = 2, s1 = 1

Using `bltu`
```
.data
prompt1: .string "'s0' is not less than 's1'"
prompt2: .string "'s0' is less than 's1'"

.text
main:
    li s0, 2 # int a = 1
    li s1, 3 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    # sltu t0, s0, s1 # s0 < s1 == 1
    # beq t0, t1, out2
    
    bltu s0, s1, out2
    
    j out1

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```
Using `non-pseudoinstruction implementation`

```
.data
prompt1: .string "'s0' is not less than 's1'"
prompt2: .string "'s0' is less than 's1'"

.text
main:
    li s0, 2 # int a = 1
    li s1, 3 # int b = 2
    li t0, 0 # int x = 0
    li t1, 1 # int flag = 1
    
    sltu t0, s0, s1 # s0 < s1 == 1
    beq t0, t1, out2
    
    # blt s0, s1, out2
    
    j out1

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```
QED.

</details>

<details>

<summary>Branch Not Equal Unsigned (bne)</summary>
<hr>

The non-pseudoinstructions used to implement `bne` is the following:
- `beq` - Branch Equal to
- `xori` - XOR immediate


```
<------- Using BNE -------->

bne s0, s1, <label>
```
This instruction compares two (2) registers `s0` and `s1` if they are not equal then it will branch/jump to the `<label>` passed otherwise, move to the next instruction.

```
<------- Implementing BNE -------->

# load the registers first

li s0, 0 # int a = 0
li s1, 0 # int a = 0
li s2, 1 # bool true
li t0, 0 # int x = 0

# create equal using bitwise
slt t0, s0, s1 # s0 < s1
slt t1, s1, s0 # s0 > s1
or t2, t0, t1 # ((s0 < s1) || (s0 > s1)) == (s1 != s0)
beq t2, s2, <label> 
```
1. We first load the registers to `zero` for initialization.
2. Compare `s0` and `s1` using less than hence, `s0 < s1` then store its evaluation to `t0`. 
3. Reverse the position of registers then compare using less than hence, `s1 < s0 ` which is just `s0 > s1` then store its evaluation to `t1`.
4. To achieve `s0 != s1` we can make use of `OR` notice that if either of the conditions is true, then it implies that `s1` and `s0` are not equal. Hence, `((s0 < s1) || (s0 > s1))` then store its evaluation to `t2`.
5. Now that we have `s0 != s1`, we can use `beq` we compare `t2` to `s2`. `s2` is (`boolean`) true that is hardcoded in 1. So the return of `t2` must be 1 also in order to satisfy the condition `s0 != s1` otherwise, fails the condition.


### USE EXAMPLE 
#### testcases: 
- s0 = 1, s1 = 2
- s0 = 1, s1 = 1
- s0 = 2, s1 = 1

Using `bne`
```
`.data
prompt1: .string "'s0' is not equal (bne) to 's1'"
prompt2: .string "'s0' is equal (beq) to 's1'"

.text
main:
    li s0, 0 # int a = 0
    li s1, 0 # int a = 0
    li s2, 1 # bool true
    li t0, 0 # int x = 0

    # create equal using bitwise
    # slt t0, s0, s1 # s0 < s1
    # slt t1, s1, s0 # s0 > s1
    # or t2, t0, t1 # ((s0 < s1) || (s0 > s1)) == (s1 != s0)
    # beq t2, s2, out1
    
    bne s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall

```
Using `non-pseudoinstruction implementation`

```.data
prompt1: .string "'s0' is not equal (bne) to 's1'"
prompt2: .string "'s0' is equal (beq) to 's1'"

.text
main:
    li s0, 0 # int a = 0
    li s1, 0 # int a = 0
    li s2, 1 # bool true
    li t0, 0 # int x = 0

    # create equal using bitwise
    slt t0, s0, s1 # s0 < s1
    slt t1, s1, s0 # s0 > s1
    or t2, t0, t1 # ((s0 < s1) || (s0 > s1)) == (s1 != s0)
    beq t2, s2, out1
    
    # bne s0, s1, out1
    
    j out2

out1:
    li a7, 4
    la a0, prompt1
    ecall
    
    j end

out2:
    li a7, 4
    la a0, prompt2
    ecall

end:
    li a7, 10
    ecall
```
QED.
 
</details>