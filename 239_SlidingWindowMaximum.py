from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        for i, num in enumerate(nums):
            if window and i - window[0] >= k:
                window.pop(0)
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
