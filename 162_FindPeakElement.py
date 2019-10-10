class Solution:
    def findPeakElement(self, nums):
        l = len(nums)
        for i in range(1, l - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return [0, l - 1][nums[0] < nums[l - 1]]

    def findPeakElement2(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
