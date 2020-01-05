class Solution:
    def maxSubArray(self, nums):
        if max(nums) < 0:
            return max(nums)
        localMax, globalMax = 0, 0
        for x in nums:
            localMax = max(0, localMax + x)
            if localMax > 0:
                globalMax = max(localMax, globalMax)
        return globalMax

    def maxSubArray2(self, nums):
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)
