class Solution:
    def subsets(self, nums):
        ans = []

        self.dfs(nums, ans, [], 0)

        return ans

    def dfs(self, nums, ans, temp, index):
        if index == len(nums):
            ans.append(temp.copy())
            return
        self.dfs(nums, ans, temp, index + 1)
        temp.append(nums[index])
        self.dfs(nums, ans, temp.copy(), index + 1)
        temp.pop()

    def subsets2(self, nums):
        ans = [[]]

        for num in nums:
            ans = ans + [x + [num] for x in ans]
        return ans
