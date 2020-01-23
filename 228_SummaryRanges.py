class Solution(object):
    def summaryRanges(self, nums):
        length = len(nums)
        res = []
        i = 0
        while i < length:
            start = nums[i]
            while i + 1 < length and nums[i + 1] - nums[i] == 1:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(end))
            i += 1
        return res
