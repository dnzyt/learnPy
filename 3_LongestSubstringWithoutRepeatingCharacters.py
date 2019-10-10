class Solution:
    def longestSubstring(self, s):
        max_len = 0
        d = {}
        start = -1

        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
            else:
                max_len = max(i - start, max_len)
            d[s[i]] = i
        return max_len
