class Solution:
    def moveZeros(self, nums):
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
