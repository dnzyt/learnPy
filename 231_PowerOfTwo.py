class Solution:
    def isPowerOfTwo(self, n):
        if n < 2:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo2(self, n):
        return n > 0 and (n & (n - 1)) == 0
