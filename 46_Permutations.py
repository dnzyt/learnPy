class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        answer = []
        for i, num in enumerate(nums):
            for y in self.permute(nums[:i] + nums[i + 1:]):
                answer.append([num] + y)
        return answer
