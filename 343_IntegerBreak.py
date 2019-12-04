class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [0 for i in range(n + 1)]
        memo[0] = 1
        memo[1] = 1
        memo[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                memo[i] = max([memo[i], j * memo[i - j], j * (i - j)])
        return memo[n]
