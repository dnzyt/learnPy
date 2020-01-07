class Solution(object):
    def largestNumber(self, nums):
        nums = map(str, nums)
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        return "0" if nums[0] == "0" else "".join(nums)

