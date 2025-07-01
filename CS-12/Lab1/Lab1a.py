def safe_jumps(H: list[int]):
    ret = [0] * len(H)
    for i in range(len(H)):
        for j in range(len(H)):
            if i != j and is_safe(H, i, j):
                ret[i] += 1
    return ret
def is_safe(H, i, j):
    if H[i] == H[j]:
        return True
    elif H[i] > H[j]:
        if i < j and all([H[j] > top for top in H[i+1:j]]):
            return True
        elif j < i and all([H[j] > top for top in H[j+1:i]]):
            return True
            
def test_cases():
    assert safe_jumps([100, 300, 200]) == [0, 2, 0]
    assert safe_jumps([300, 100, 200]) == [2, 0, 1]
    assert safe_jumps([100, 100, 100, 20, 50, 60, 30]) == [2, 2, 5, 0, 1, 2, 0]
test_cases()