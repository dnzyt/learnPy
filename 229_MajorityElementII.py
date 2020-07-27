from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        c = Counter(nums)
        return [k for (k, v) in c.items() if v > (l / 3)]


    def majorityElement2(self, nums: List[int]) -> List[int]:
        # 结果最多含有两个值
        num1, num2 = 0, 0
        c1, c2 = 0, 0
        # 找到出现次数最多的两个值
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
            elif c1 == 0:
                num1 = num
                c1 = 1
            elif c2 == 0:
                num2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
        res = []
        if c1 > (len(nums) // 3):
            res.append(num1)
        if c2 > (len(nums) // 3):
            res.append(num2)
        return res