class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(list(set(nums)))

        if len(l) < 3:
            return l[-1]
        else:
            return l[-3]
