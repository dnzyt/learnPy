from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        curr, start, end = 0, 0, len(nums) - 1
        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[start] = nums[start], nums[curr]
                curr += 1
                start += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
