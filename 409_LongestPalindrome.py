class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        flag = 0
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for k in d:
            if d[k] % 2 == 0:
                res += d[k]
            else:
                res += (d[k] - 1)
                flag = 1
        return res + flag
