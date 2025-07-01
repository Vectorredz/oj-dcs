
<summary>Item 01</summary>

Notice that upon calling `fact_iter` it will allocate 12 bytes of stack memory for `ra`, `s0` and `s1` this is done for every call on `fact_iter`. However, in the iterative case, `fact_iter` is only called once by main and proceeds to the loop proper. label `fact_iter__loop` do most of the instructions for the algorithm of getting the factorial of the passed `s0`. It doesn't either reallocate or deallocate memory from stack. Rather, after reaching the `guard condition` in the loop it will branch to `fact_iter__ret` that does popping operation of the allocated stack from the `fact_iter`. 

**Expression**
$$
F(N) = \text{fact\_iter}() + \text{fact\_iter\_\_ret}()
$$

whereas, calling `fact_iter` will execute `sw` three (3) times and calling branching to `fact_iter__ret` will execute three (3) times.

Hence total number of executions of `lw` and `sw` resulting from executing `li a0, N` and `call_fib_iter` is:

$$
F(N) = [sw(ra, \, 0(sp)) + sw(s0, \, 4(sp)) + sw(s1, \, 8(sp))] + [lw(ra, \, 0(sp)) + lw(s0, \, 4(sp)) + lw(s1, \, 8(sp))]
$$

**Asymptotic Rate of Growth**

Given in the derived expression, the total number of `lw` and `sw` is constant purely independent of the `N`.

In Asymptotic notation, this is represented as:

$$
O(6) = O(1) \\
$$

Hence, the asymptotic notation of the derived expression: 

$$
F(N) = O(1)
$$

<summary>Item 02</summary>

Notice that upon calling the `fact_rec` it will immediately execute two (2) `sw` instructions, allocating 8 bytes for `ra` and `s0`.  After these first `push` instructions it will proceed to the factorial algorithm that increments `t0` from `0 -> N`. This is the base case of the recursion. Upon reaching `t0 = N` it will branch to the `fact_rec__ret_base` and reinitialize `a0` to `1` in order to return 1. After that it will proceed to the next function, `fact_rec__ret` that will do the popping operation. It will execute `lw` two (2) times then returns to the caller. 

**Expression**
$$
F(N) = F(N-1) + sw + lw
$$

where `sw = 2` and `lw = 2`:

$$
F(N) = F(N-1) + 2 + 2
$$


**Asymptotic Rate of Growth**
$$
T(N) = T(N-1) + 2 + 2\\
T(N-1) = T(N-2) + 4 + 4\\ 
...\\
T(N-k) = T(N-k) + 2k + 2k \\
T(N-k) = T(N-k) + 4k \\
$$

when k = N,

$$
T(N-N) = T(0) = 1
$$

hence, in Asymptotic notation,
$$
O(N) = T(0) + 4n \\
O(N) = 1 + 4n \\
O(N) = 4n \\
O(N) \\
$$

thus, the asymptotic notation of the derived expression is:
$$
F(N) = O(N)
$$


<summary>Item 03
</summary>

<summary>Item 04
</summary>

**Expression**

$$
F(N) = fact\_iter() + fact\_iter\_\_loop() + fact\_iter\_\_ret()
$$

where the number of instructions from `fact_iter() = 6`, `fact_iter__loop() = 4N`, and `fact_iter__ret() = 5` hence,

$$
F(N) = 6 + 4N + 5 \\ 
F(N) = 4N + 11
$$

**Asymptotic Rate of Growth**

$$
F(N) = 4N + 11 \\
F(N) = N \\
F(N) = N \\ 
$$

hence, in Asymptotic Notation the derived expression,

$$
F(N) = O(N)
$$

<summary>Item 05
</summary>

**Derived Expression**

$$
F(N) = (5) + (6) + F(N-1) + fact\_rec\_\_ret\_base() + fact\_fact\_rec\_\_ret()
$$

where `5` corresponds to the number of instructions before calling proceeding the instruction that checks the base case, `bge`. `F(n-1)` corresponds to the recursive step of the `fact_ret`. `` corresponds to the operation after the recursive step. While `fact_rec__ret_base()` calls have only `1` instruction everytime it reached the base case. Lastly, `fact_rec__ret_base` has`4` instructions for popping and returning to the callee. 

$$
F(N) = (5) + (6) + F(N-1) + (1) + (4)
F(N) = F(N-1) + 16
$$

**Asymptotic Rate of Growth**
$$
T(N) = T(N-1) + 16 \\
T(N) = T(N-2) + 32 \\
F(N) = N \\ 
$$

hence, in Asymptotic Notation the derived expression,

$$
F(N) = O(N)
$$








