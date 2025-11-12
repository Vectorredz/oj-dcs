CONST = 1_000_000_000

def num_slimes_after(sizes: list[int], d: int) -> int:
    new_sizes: list[int] = sizes
    while (d):
        temp_sizes: list[int] = []
        for size in new_sizes:
            if (_multiple_digits(size) > 1): # two digits
                _split_digits(temp_sizes, size)
            else: # single digit
                temp_sizes.append(size * 2)
        new_sizes = temp_sizes # new size per day
        d-=1 
    print(new_sizes)
    return int(len(new_sizes) % CONST)

def _multiple_digits(num: int) -> int:
    i = 0
    while(num != 0):
        num //= 10
        i+=1
    return i
        
def _split_digits(new_sizes: list[int], num: int):
    if (num == 0):
        return new_sizes
    else:
        digit: int = num % 10
        num //= 10
        if (digit != 0):
            new_sizes.append(digit)
        _split_digits(new_sizes, num)
        return new_sizes
        
        
# print(_split_digits(new_sizes, 232))
# print(num_slimes_after([3, 6], 2))
# assert num_slimes_after([10, 10], 2) == 2
# assert num_slimes_after([0, 0], 2) == 2
# result = num_slimes_after([9, 9, 9], 4)

# assert result == 2, f"Expected 2 but got {result}"

# [1 8, 1 8, 1 8], [1, 8]