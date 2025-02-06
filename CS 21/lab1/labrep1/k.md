# Laboratory 1 
## Item 4 - Branch Pseudoinstructions

<details>
<summary>Branch Greater Than Or Equal (bge)</summary>
<hr>

(1) One way we can implement BGE is using non-pseudoinstructions.

The non-pseudoinstructions used:
- `slt` - Set Less Than
- `xori` - XOR immediate
- `bnez` - Branch Not Equal To Zero



Suppose you have two (2) registers `s0` and `s1` . Using the Pseudoinstructions we can implement the **BGE** as the following:

```
# -- Using BGE --

bge s0, s1, <label>
```
What this do is that if `s0` is greater than or equal `s1` it will branch/jump out to the `label` passed.

```
# -- Implementing BGE --

# load the registers first

li s0, 0
li s1, 0
li t0, 0

slt t0, s0, s1 # s0 < s1
xori t0, t0, 1 # s0 >= s1
bnez t0, <label> # t0 != 0
```
1. We first load the registers to `zero` for initialization.
2. Reverse the `s1` and `s0` location in `slt` command to create `s0 > s1`
3. Store the evaluation to a temporary register `t0`.
4. using the non-pseudoinstruction `xori` we negate `t0` register to get `>=`. Hence, `t0` now contains the evaluation of `s0 >= s1`
5. Use non-pseudoinstruction `bnez` to simulate the brancing if a condition is not meant.
   -  `bnez` takes 1 register and if it is not equal to `0` then it will branch out to the `label` passed.
   -  In our case, we use resulting evaluation `t0` register to compare it to `0`
 
 QED.
</details>

<details>

<summary>Branch Greater Than Or Equal Unsigned (bgeu) </summary>
 
Similar to the first item, we can make use of other non-pseudoinstructions. 

The non-pseudoinstructions used:
- `sltu` - Set Less Than Unsigned
- `xori` - XOR immediate
- `bnez` - Branch Not Equal To Zero

</details>

<details>

<summary>Branch Less than (blt)</summary>

The non-pseudoinstructions used:
- `slt` - Set Less Than
- `bnez` - Branch Not Equal To Zero

 
</details>

<details>

<summary>Branch Less Than Unsigned (bltu)</summary>
 
</details>

<details>

<summary>Branch Not Equal Unsigned (bne)</summary>
 
</details>