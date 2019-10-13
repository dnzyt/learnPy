class Solution:
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            temp1 = self.getLongest(s, i, i)
            len1 = len(temp1)
            if len1 > len(palindrome):
                palindrome = temp1
            temp2 = self.getLongest(s, i, i + 1)
            len2 = len(temp2)
            if len2 > len(palindrome):
                palindrome = temp2
        return palindrome

    def getLongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]
