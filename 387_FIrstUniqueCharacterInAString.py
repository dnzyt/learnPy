class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        lookup = Counter(s)
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i
        return -1
