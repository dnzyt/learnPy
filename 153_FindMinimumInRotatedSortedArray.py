from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(start, end):
            if start == end:
                return start
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                return helper(mid + 1, end)
            elif nums[mid] < nums[start]:
                return helper(start, mid)
            else:
                return start
        idx = helper(0, len(nums) - 1)
        return nums[idx]
