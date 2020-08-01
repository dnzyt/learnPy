from typing import List


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res = 0
    temp = 0
    for idx, num in enumerate(nums):
        if num == 0:
            res = max(res, temp)
            temp = 0
        elif num == 1:
            temp += 1
    return max(res, temp)
