class Solution:
    def isPowerOfFour(self, num):
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        return num == 1
