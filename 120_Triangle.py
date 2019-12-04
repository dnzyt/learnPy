class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = triangle[-1]
        for i in reversed(range(n - 1)):
            for idx in range(i + 1):
                dp[idx] = min(dp[idx], dp[idx + 1]) + triangle[i][idx]
        return dp[0]
