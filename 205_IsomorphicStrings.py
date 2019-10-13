class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            else:
                if d1[s[i]] != t[i]:
                    return False
            if t[i] not in d2:
                d2[t[i]] = s[i]
            else:
                if d2[t[i]] != s[i]:
                    return False
        return True

    def isIsomorphic2(self, s, t):
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if d1.get(a, -1) != d2.get(b, -1):
                return False
            d1[a] = i
            d2[b] = i
        return True
