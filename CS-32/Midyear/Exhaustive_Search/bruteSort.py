nums: list[int] = [4,7,1,2,3,4,0]

def selectionSort(l: list[int]) -> list[int]:
    n: int = len(l)
    for i in range(n):
        key: int = i
        for j in range(i+1, n):
            if (l[key] > l[j]):
                key = j
        # swap
        l[key], l[i] = l[i], l[key]
        
    return l

def bubbleSort(l: list[int]) -> list[int]:
    n: int = len(l)
    for i in range(n):
        swapped: bool = False
        for j in range(n-i-1):
            if (not swapped and l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
            elif swapped:
                break
    return l

print(bubbleSort(nums))
            
