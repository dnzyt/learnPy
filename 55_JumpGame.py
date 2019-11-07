class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        endReachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= endReachable:
                endReachable = i
        return endReachable == 0
