class Solution:
    def convertToTitle(self, n):
        res, num = '', n
        while num != 0:
            res += chr((num - 1) % 26 + ord('A'))
            num = (num - 1) // 26
        return res[::-1]
