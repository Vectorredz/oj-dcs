def max_enjoyment(nums:list[int]):
    if len(nums) > 3:
        sure_nums = sorted(nums)[:3]
        for k in sure_nums:
            nums.pop(nums.index(k))
    maxSum = nums[0]
    currSum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            currSum += sum(nums[i:j+1])
            if currSum < 0:
                currSum = 0
            maxSum = max(maxSum, currSum)
    return maxSum

def test_cases():
    max_enjoyment([143]) == 143
    max_enjoyment([-31415, -92653]) == 0
    max_enjoyment([-100, 10, 0, 10, -100]) == 20
    max_enjoyment([-1, 9, -2, -1, -2, 3, -1, -2, 4, -6, 5, -2, 1, -2]) == 17
test_cases()