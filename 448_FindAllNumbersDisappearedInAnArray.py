from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set([i for i in range(1, len(nums) + 1)])
        b = set(nums)
        return list(s - b)
