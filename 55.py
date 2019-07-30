def canJump(nums):
    j = 0
    for i, x in enumerate(nums):
        if j < i: return False
        j = max(j, i+x)
    return True


#Go backwards
def canJump(self, nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1)[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal