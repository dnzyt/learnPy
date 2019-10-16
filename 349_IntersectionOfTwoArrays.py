class Solution:
    def intersection(self, nums1, nums2):
        lookup = set()
        for i in nums1:
            lookup.add(i)

        res = []
        for i in nums2:
            if i in lookup:
                res.append(i)
                lookup.discard(i)
        return res
