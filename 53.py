class Solution:
    # @param {integer[]} nums
    # @return {integer}


    def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) // 2

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)