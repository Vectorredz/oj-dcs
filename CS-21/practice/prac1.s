

// lb <t0>, <0><t1>
/*
12-bits immediate
20-bits are extended

for example:
t1 = 0000 0000 1111 = 15
t0 = 0000 0000 0000 0000 | 0000 0000 1111

lb t0, 0(t1)
-> t0, imm

*/