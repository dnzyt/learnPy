class Solution(object):
    def maxProduct(self, nums):
        res = nums[0]
        currMax, currMin = nums[0], nums[0]
        for i in range(1, len(nums)): 
            temp = currMax
            currMax = max(nums[i], max(currMax * nums[i], currMin * nums[i]))
            currMin = min(nums[i], min(temp * nums[i], currMin * nums[i]))
            res = max(res, currMax)
        return res
    
