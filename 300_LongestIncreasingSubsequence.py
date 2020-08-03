from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        return 0 if len(dp) == 0 else max(dp)
