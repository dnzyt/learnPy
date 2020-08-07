from typing import List


class Solution:
    # 找出每一个相同节点之前的最大值
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        a, b = 0, 0

        while i < n or j < m:
            if i < n and (j == m or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < m and (i == n or nums2[j] < nums1[i]):
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i]
                i += 1
                j += 1

        return max(a, b) % (10 ** 9 + 7)
