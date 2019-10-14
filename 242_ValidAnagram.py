class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = 0
            if t[i] not in lookup:
                lookup[t[i]] = 0
            lookup[s[i]] += 1
            lookup[t[i]] - + 1
        for k in lookup:
            if lookup[k] != 0:
                return False
        return True
