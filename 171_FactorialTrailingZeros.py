class Solution:
    def trailingZeroes(self, n):
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)
