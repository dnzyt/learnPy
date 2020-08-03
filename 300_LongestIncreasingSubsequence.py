from typing import List
from bisect import bisect_left


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

    # Nlog(N)的解法
    # 维护一个数组lis，如果num比数组里的数都大，那么加入到lis的末尾
    # 不然在lis中找到比num大的最小的数的位置，进行替换
    # 最后返回lis长度

    def lengthOfLIS2(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return len(lis)
