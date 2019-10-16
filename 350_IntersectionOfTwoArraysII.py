import collections


class Solution:
    def intersect(self, nums1, nums2):
        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1
        res = []
        for i in nums2:
            if lookup[i] > 0:
                lookup[i] -= 1
                res.append(i)
        return res
