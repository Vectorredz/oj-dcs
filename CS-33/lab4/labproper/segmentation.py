from math import floor, log2

def byte(arr):
    return 1024 * arr if type(arr) == int else list(map(lambda x: x * 1024, arr)) 
    
# given
BITS = 16
PA = byte([4,42,-1,37])
base = byte([4,42,-1,37])
size = byte([5,9,-1,4])

def solver(item):
    va = item
    seg = int(va) >> (BITS-2)
    offset = va & (0x3FFF)
    # print(0x3fff)
    # print(seg, hex(item), f"0x{item:016b}", offset, size[seg])
    if seg <= 1:
        # explicit approach 
        paddr = base[seg] + offset
        if offset >= size[seg]:
            return "invalid"
        return hex(paddr)
    
    elif seg == 3:
        # implicit approach
        diff = abs(byte(BITS) - offset)
        # print(diff, size[seg],  byte(BITS), offset)
        if diff > size[seg]:
            print(diff, size[seg])
            return "invalid"
        else:
            paddr = base[seg] - diff
            # print(base[seg] -  diff, bin(va), len("11101011001110"), (int("0b11101011001110", 2)))
            # print(base[seg], diff)
            return hex(paddr)
    else:
        return "invalid"
answers = []

items = [0x0001, 0x4111, 0xc0c0, 0x116e, 0xface, 0x3eef, 0x3abe, 0x0424]
for elem in items:
    answers.append(solver(elem))
print(answers)
