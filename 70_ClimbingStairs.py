class Solution:
    def climbStairs(self, n):
        prev, current = 0, 1
        for _ in range(n):
            prev, current = current, prev + current
        return current
