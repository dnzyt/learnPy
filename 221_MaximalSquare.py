class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j] * dp[i][j])
        return ans
