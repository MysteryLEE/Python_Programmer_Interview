def rob(nums):
    prev = curr = 0
    for num in nums:
        curr, prev = max(curr, prev+num), curr
    return curr